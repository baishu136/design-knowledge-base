"""Audit schemas' supported subset, local links, IDs, fixed-source hashes and numeric evidence.
Only reads upstream files; writes knowledge-base VALIDATION.md and validation-results.json.
"""
from pathlib import Path
from urllib.parse import unquote
import json, re, hashlib, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
errors=[]; checks={}; warnings=[]
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def check(condition,message):
    if not condition:errors.append(message)
def schema_check(value,schema,where):
    if '$ref' in schema:
        return schema_check(value,load(ROOT/'schemas'/schema['$ref']),where)
    types=schema.get('type')
    def istype(t):
        return {'object':isinstance(value,dict),'array':isinstance(value,list),'string':isinstance(value,str),'integer':isinstance(value,int) and not isinstance(value,bool),'number':isinstance(value,(int,float)) and not isinstance(value,bool),'boolean':isinstance(value,bool),'null':value is None}[t]
    if types:
        ok=any(istype(t) for t in ([types] if isinstance(types,str) else types))
        check(ok,f'{where}: type {types}')
        if not ok:return
    if 'enum' in schema:check(value in schema['enum'],f'{where}: enum')
    if isinstance(value,dict):
        for k in schema.get('required',[]):check(k in value,f'{where}: missing {k}')
        for k,s in schema.get('properties',{}).items():
            if k in value:schema_check(value[k],s,where+'/'+k)
    if isinstance(value,list):
        check(len(value)>=schema.get('minItems',0),f'{where}: minItems')
        for i,v in enumerate(value):
            if 'items' in schema:schema_check(v,schema['items'],where+'/'+str(i))
    if isinstance(value,str) and 'pattern' in schema:check(re.search(schema['pattern'],value) is not None,f'{where}: pattern {schema["pattern"]}')
    if isinstance(value,(float,int)) and 'minimum' in schema:check(value>=schema['minimum'],f'{where}: minimum')

alljson=list(ROOT.rglob('*.json'))
for f in alljson:
    try:load(f)
    except Exception as e:errors.append(f'JSON parse {f}: {e}')
checks['json_files_parsed']=len(alljson)
for pattern,sch in [('projects/*/manifest.json','manifest'),('projects/*/animations/*/spec.json','animation'),('projects/*/components/*/spec.json','component'),('projects/*/design-language/tokens.json','tokens'),('projects/*/animations/*/examples/example.json','example'),('CATALOG.json','catalog')]:
    for f in ROOT.glob(pattern):schema_check(load(f),load(ROOT/'schemas'/f'{sch}.schema.json'),f.relative_to(ROOT).as_posix())

catalog=load(ROOT/'CATALOG.json'); ids=[r['id'] for r in catalog['resources']]
check(len(ids)==len(set(ids)),'Duplicate catalog ID')
checks['indexed_resources']=len(ids)
indexed=set()
for r in catalog['resources']:
    for target in [r['doc_path'],r['spec_path'],*r['example_paths'],*r['documents']]:
        if target is None:continue
        check(not Path(target).is_absolute() and '\\' not in target and '..' not in Path(target).parts,'Unsafe catalog path '+target)
        check((ROOT/target).is_file(),'Missing catalog path '+target);indexed.add(target)
    for rid in r['related_resource_ids']:check(rid in ids,'Missing related ID '+rid)
    if r['spec_path'] and r['resource_type'] in ['animation','component','example']:
        check(load(ROOT/r['spec_path'])['id']==r['id'],'ID differs from spec '+r['id'])
for f in ROOT.rglob('*.md'):
    # Validation report is written at the end; an existing copy is still indexed.
    check(f.relative_to(ROOT).as_posix() in indexed,'Markdown not indexed '+str(f.relative_to(ROOT)))
    body=f.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)',body):
        if re.match(r'^(https?://|mailto:|#)',target):continue
        local=unquote(target.split('#')[0].strip('<>'))
        if not local:continue
        check((f.parent/local).resolve().is_file(),'Broken Markdown link '+str(f.relative_to(ROOT))+' -> '+local)

manifests={f.parent.name:load(f) for f in ROOT.glob('projects/*/manifest.json')}
source_count=0;file_count=0
for pid,manifest in manifests.items():
    print(json.dumps({'auditing_project':pid},ensure_ascii=False),flush=True)
    upstream=WORK/manifest['source_snapshot']
    check(upstream.is_dir(),'Missing snapshot '+str(upstream))
    sources=load(ROOT/f'projects/{pid}/references/source-map.json')
    cache={}
    for ref in sources:
        schema_check(ref,load(ROOT/'schemas/source.schema.json'),pid+' source')
        f=upstream/ref['path']
        check(f.is_file(),'Missing upstream '+pid+'/'+ref['path'])
        if not f.exists():continue
        if ref['path'] not in cache:cache[ref['path']]=f.read_bytes()
        content=cache[ref['path']]
        check(hashlib.sha256(content).hexdigest()==ref['sha256'],'Source drift '+pid+'/'+ref['path'])
        check(ref['commit']==manifest['commit'],'Commit mismatch '+pid+'/'+ref['path'])
        check(1<=ref['line']<=len(content.decode('utf-8-sig').splitlines()),'Source line out of bounds '+ref['path'])
        check(f'/blob/{manifest["commit"]}/' in ref['url'],'Non-pinned source URL '+ref['url'])
        source_count+=1
    file_count+=len(cache)
    # The entire supported-text inventory is hashed, so unchanged source is independently checked.
    inventory=load(ROOT/f'projects/{pid}/references/file-inventory.json')['files']
    for item in inventory:
        f=upstream/item['path']
        check(f.is_file(),'Inventory source missing '+str(f))
        if f.exists():check(hashlib.sha256(f.read_bytes()).hexdigest()==item['sha256'],'Inventory source modified '+str(f))
    checks[pid+'_text_snapshot_files_checked']=len(inventory)
    if pid=='mihon':
        result=subprocess.run(['git','-C',str(upstream),'status','--porcelain'],capture_output=True,text=True)
        check(result.returncode==0 and not result.stdout.strip(),'Mihon worktree changed')
    check(len(list((ROOT/f'projects/{pid}/animations').glob('*/spec.json')))==manifest['coverage']['animations'],'Animation count mismatch '+pid)
    check(len(list((ROOT/f'projects/{pid}/components').glob('*/spec.json')))==manifest['coverage']['components'],'Component count mismatch '+pid)
checks['source_records_checked']=source_count;checks['unique_cited_source_files']=file_count

# Independent bindings join a source regex capture to an emitted spec parameter.
# Each animation has at least one binding. Non-explicit/delegated values stay unknown.
bindings=[
 ('mihon','adaptive-sheet','presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt',r'durationMillis = (350)','timing.duration_ms'),
 ('mihon','reader-bars','app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt',r'tween<IntOffset>\((200)\)','timing.duration_ms.slide'),
 ('mihon','reader-bars','app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt',r'tween<Float>\((150)\)','timing.duration_ms.fade'),
 ('mihon','fast-scroller','presentation-core/src/main/java/tachiyomi/presentation/core/components/VerticalFastScroller.kt',r'ThumbLength = (48)\.dp','properties.thumb_length_dp'),
 ('mihon','combined-progress','presentation-core/src/main/java/tachiyomi/presentation/core/components/CircularProgressIndicator.kt',r'tween\((2000), easing = LinearEasing\)','timing.duration_ms.rotation'),
 ('mihon','button-elevation','presentation-core/src/main/java/tachiyomi/presentation/core/util/Elevation.kt',r'durationMillis = (120)','timing.duration_ms.incoming'),
 ('cherry-studio-app','menu-panel','packages/ui/src/motion.ts',r'slow: (350)','timing.duration_ms.open'),
 ('cherry-studio-app','menu-panel','packages/ui/src/motion.ts',r'base: (250)','timing.duration_ms.close'),
 ('cherry-studio-app','menu-panel','packages/ui/src/components/menu/menu-motion.ts',r'menuRestingScale = (0\.97)','properties.scale.0'),
 ('cherry-studio-app','rotating-text','packages/ui/src/motion.ts',r'damping: (31\.5)','timing.spring.damping'),
 ('cherry-studio-app','rotating-text','packages/ui/src/components/text-animation/text-animation.tsx',r'ENTER_FADE_DELAY = (60)','timing.delay_ms.enter_fade'),
 ('cherry-studio-app','effort-slider','src/frontend/features/chat/components/ChatInput/effortSlider/utils/constants.ts',r'duration: (200)','timing.duration_ms'),
 ('cherry-studio-app','image-zoom','src/frontend/components/ArtifactPreview/components/ArtifactImageViewer/ZoomableImage.tsx',r'DOUBLE_TAP_SCALE = (2\.5)','end_state.doubleTapScale'),
 ('cherry-studio-app','native-bottom-sheet','packages/ui/src/components/bottom-sheet/bottom-sheet.tsx',r'MAX_CARD_WIDTH = (720)','properties.max_width'),
 ('cherry-studio-app','foil-loader','packages/ui/src/components/loading/image-generation-loader.tsx',r'CLOCK_WRAP_SECONDS = (1200)','properties.clock_wrap_seconds'),
 ('cherry-studio','resource-pane','src/renderer/components/chat/shell/paneLayout.ts',r'duration: (0\.3)','timing.duration_ms',1000),
 ('cherry-studio','dialog','packages/ui/src/components/primitives/dialog.tsx',r'animation-duration-\[(260)ms\]','timing.duration_ms.content_open'),
 ('cherry-studio','selector-shell','src/renderer/assets/styles/animation.css',r'animation-selector-shell-panel-enter (150)ms','timing.duration_ms.open'),
 ('cherry-studio','composer-dock','src/renderer/assets/styles/animation.css',r'animation-chat-composer-dock-down (220)ms','timing.duration_ms'),
 ('cherry-studio','smooth-scroll','src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts',r'DEFAULT_FRAMES = (50)','timing.frames'),
 ('cherry-studio','text-shimmer','src/renderer/assets/styles/animation.css',r'animation-shimmer (3)s linear','timing.duration_ms',1000),
 ('cherry-studio','heatmap-entry','src/renderer/assets/styles/animation.css',r'animation-usage-heatmap-cell-enter (520)ms','timing.duration_ms'),
 ('droiddeck','focus-glide','app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt',r'minOf\(left, (0\.004)f\)','properties.integration_substep_ms',1000),
 ('droiddeck','focus-glide','app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt',r'lead\(\) = Edge\(0\.62f, (700)f\)','timing.spring.lead.stiffness'),
 ('droiddeck','chip-glide','app/src/main/java/com/droiddeck/launcher/ui/SharedMotion.kt',r'delay\(Motion.ms\((40)\)','timing.delay_ms.trail'),
 ('droiddeck','launch-flood','app/src/main/java/com/droiddeck/launcher/ui/LaunchFlood.kt',r'dampingRatio = (0\.48)f','timing.spring.dampingRatio'),
 ('droiddeck','page-flood','app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt',r'PAGE_RETURN_MS = (900)','timing.duration_ms.retention'),
 ('droiddeck','button-press','app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt',r'if \(pressed\) (0\.955)f','end_state.pressed_scale'),
 ('droiddeck','lift-sheet','app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt',r'PIECES = (12)','properties.pieces'),
 ('droiddeck','lift-sheet','app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt',r'val flick = with\(density\) \{ (600)\.dp','properties.flick_threshold_dp_per_s'),
 ('droiddeck','inner-gamer','app/src/main/java/com/droiddeck/launcher/ui/Theme.kt',r'RGB_HUE_STEP = (3)f','properties.hue_step_degrees'),
 ('droiddeck','logo-throbber','app/src/main/java/com/droiddeck/launcher/ui/Throbber.kt',r'LOOP_MS = (1900)','timing.duration_ms'),
 ('droiddeck','session-activity','app/src/main/res/anim/session_rise.xml',r'android:duration="(380)"','timing.duration_ms.enter'),
 ('droiddeck','session-activity','app/src/main/res/anim/session_sink.xml',r'android:duration="(320)"','timing.duration_ms.exit'),
]
evidence=[]
for binding in bindings:
    pid,slug,path,pattern,pointer,*factor=binding
    source=(WORK/manifests[pid]['source_snapshot']/path).read_text(encoding='utf-8-sig')
    match=re.search(pattern,source)
    check(match is not None,'Missing numeric evidence '+pid+'/'+slug+': '+pattern)
    if not match:continue
    actual=load(ROOT/f'projects/{pid}/animations/{slug}/spec.json')
    for k in pointer.split('.'):actual=actual[int(k)] if isinstance(actual,list) else actual[k]
    expected=float(match.group(1))*(factor[0] if factor else 1)
    check(actual==expected,'Parameter differs '+pid+'/'+slug+'/'+pointer)
    evidence.append(dict(project=pid,animation=slug,source_path=path,line=source[:match.start()].count('\n')+1,pattern=pattern,spec_pointer=pointer,value=actual))
# Check delegated values were not filled with guessed numbers.
for pid,slug in [('mihon','shared-axis-navigation'),('cherry-studio-app','image-zoom'),('cherry-studio-app','native-bottom-sheet'),('cherry-studio','smooth-scroll')]:
    spec=load(ROOT/f'projects/{pid}/animations/{slug}/spec.json')
    check(spec['timing']['duration_ms'] is None,'Guessed duration '+pid+'/'+slug)
    if slug=='shared-axis-navigation':
        content=(WORK/manifests[pid]['source_snapshot']/'app/src/main/java/eu/kanade/presentation/util/Navigator.kt').read_text(encoding='utf-8-sig')
        check('materialSharedAxisX(' in content and 'rememberSlideDistance()' in content,'Shared-axis delegated source changed')
        evidence.append(dict(project=pid,animation=slug,delegated=True,source_path='app/src/main/java/eu/kanade/presentation/util/Navigator.kt',duration=None))
checks['parameter_evidence_bindings']=len(evidence)

runtime=subprocess.run(['node',str(ROOT/'tools/check-examples.mjs')],capture_output=True,text=True)
check(runtime.returncode==0,'Example harness failed: '+runtime.stderr)
checks['example_harness']=json.loads(runtime.stdout) if runtime.returncode==0 else runtime.stdout
droid_runtime=subprocess.run(['node',str(ROOT/'tools/check-droiddeck.mjs')],capture_output=True,text=True)
check(droid_runtime.returncode==0,'DroidDeck example harness failed: '+droid_runtime.stderr)
checks['droiddeck_example_harness']=json.loads(droid_runtime.stdout) if droid_runtime.returncode==0 else droid_runtime.stdout
for f in ROOT.glob('projects/*/animations/*/spec.json'):check(load(f)['runtime_verified'] is False,'Unexpected original app runtime claim '+str(f))
for f in ROOT.glob('projects/*/animations/*/examples/example.json'):
    ex=load(f);check(not ex['visual_runtime_verified'],'Unexpected visual runtime claim '+str(f))
    for name in ex['files']:check((f.parent/name).is_file(),'Missing example file '+name)

result=dict(date='2026-11-16',status='passed' if not errors else 'failed',checks=checks,errors=errors,warnings=warnings,parameter_evidence=evidence,limits=['No upstream application runtime','No visual verification','Native examples not compiled','JSON Schema supported-keyword subset only','Static performance analysis only'])
(ROOT/'validation-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='# 最终审计与验证\n\n状态：'+result['status']+'。\n\n'+ '\n'.join(f'- {k}：`{json.dumps(v,ensure_ascii=False)}`' for k,v in checks.items())
report+='\n\n## 审计边界\n\nJSON可解析、声明Schema子集、ID唯一、关联ID、索引路径、Markdown链接、来源Commit/行范围/SHA256、全部支持文本文件快照哈希、Mihon干净工作树、组件/动画数量、参数证据绑定与未知值防猜测均被检查。源码参数证据记录于validation-results.json。\n\n原项目未运行；Node运行3个移植内核（scroll controller、loader clock、DroidDeck单边spring），模拟多刷新步长不是实际设备FPS测试。没有截图、录屏、原生编译、GPU或FPS测试。对性能和设计意图的解释是静态分析，不是实测或官方承诺。\n\n所有原项目动画runtime_verified=false；原生和React视觉例仍unverified。静态成功不提升它们的状态。\n'
if errors:report+='\n## 失败\n\n'+'\n'.join('- '+e for e in errors)
(ROOT/'VALIDATION.md').write_text(report,encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':checks,'errors':errors[:30]},ensure_ascii=False))
sys.exit(1 if errors else 0)
