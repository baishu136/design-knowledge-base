"""Build authored research data into a traceable, indexed knowledge base. No upstream code runs."""
from pathlib import Path
import json, hashlib, re, subprocess, shutil

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
DATE = '2026-11-16'
PROJECTS = {}

def write(path, text):
    f = ROOT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text.strip() + '\n', encoding='utf-8')

def dump(path, data):
    write(path, json.dumps(data, ensure_ascii=False, indent=2))

def text_file(root, path):
    return (root / path).read_text(encoding='utf-8-sig')

def source(p, path, symbol, needle=None):
    content = text_file(p['root'], path)
    search = needle or symbol
    assert search in content, (p['id'], path, search)
    line = content[:content.index(search)].count('\n') + 1
    record = dict(path=path, symbol=symbol, line=line, commit=p['commit'],
                  sha256=hashlib.sha256((p['root']/path).read_bytes()).hexdigest(),
                  url=f"{p['repo']}/blob/{p['commit']}/{path}#L{line}")
    p['sources'][path+'#'+symbol] = record
    return record

def link_sources(refs):
    return '\n'.join(f"- [`{r['path']}:{r['line']}` — `{r['symbol']}`]({r['url']})" for r in refs)

def project(pid, root, repo, commit, version, platforms, stack, overview, dirs):
    p = dict(id=pid, root=WORK/root, repo=repo, commit=commit, version=version,
             platforms=platforms, stack=stack, overview=overview, dirs=dirs,
             sources={}, animations=[], components=[], tokens=[], docs={}, checks=[])
    PROJECTS[pid]=p
    return p

def doc(p, name, body, refs):
    p['docs'][name]=(body, refs)

def token(p, name, value, unit, use, ref, theme='all', origin='original-definition'):
    p['tokens'].append(dict(name=name,value=value,unit=unit,usage=use,theme=theme,
                            origin=origin,source=ref,verification=['source-verified']))

def animation(p, slug, name, category, refs, *, effect, trigger, start, end,
              timing, properties, mechanism, interrupt, accessibility, performance,
              use, avoid, gesture=None, sequence=None, assertions=None):
    aid=p['id']+'.animation.'+slug
    for key in ['duration_ms','delay_ms','easing','spring','repeat']:
        timing.setdefault(key,None)
    spec=dict(schema_version='1.0',id=aid,name=name,project=p['id'],category=category,
        effect=effect,applicable=use,not_applicable=avoid,trigger=trigger,start_state=start,end_state=end,
        timing=timing,properties=properties,transform_origin=None,
        keyframes_or_sequence=sequence or {'domain':'per-track normalized progress','from':start,'to':end},synchronization=mechanism,
        interruption=interrupt,gesture=gesture,accessibility=accessibility,
        dependencies=p['stack'],sources=refs,performance=dict(kind='static-analysis',notes=performance,measurements=None,verification=['inferred']),
        verification=['source-verified'],runtime_verified=False,license=p.get('license','AGPL-3.0'),
        confidence={'implementation_facts':'high: directly read fixed source','runtime_effect':'unverified','performance':'inferred; measurements required'},
        reuse='见项目 LICENSE-NOTES.md；此规格为分析总结，示例的改编状态逐文件声明。',
        unknown_fields_policy='null 表示源文件没有显式定义或本轮未追溯依赖默认值；不代表 0 或无需处理。',
        evidence_assertions=assertions or [])
    p['animations'].append((slug,spec,mechanism))
    return aid

def component(p, slug, name, refs, *, use, structure, parameters, states, api, behavior, migration, example, avoid, related=None):
    spec=dict(schema_version='1.0',id=p['id']+'.component.'+slug,name=name,project=p['id'],
        purpose=use,structure=structure,parameters=parameters,states=states,api=api,
        behavior=behavior,migration=migration,minimal_usage=example,not_applicable=avoid,
        sources=refs,related_resources=related or [],verification=['source-verified'],runtime_verified=False,
        dependencies=p['stack'],license=p.get('license','AGPL-3.0'))
    p['components'].append((slug,spec))

SEARCH = {
 'timing-spring':r'withTiming|withSpring|tween\(|spring\(|TweenSpec|animateTo\(|withDecay',
 'presence-layout':r'AnimatedVisibility|AnimatedContent|Crossfade|animateContentSize|AnimatePresence|motion\.|layoutId|LayoutAnimation|FadeIn|FadeOut',
 'gesture-scroll':r'Gesture\.|anchoredDraggable|pointerInput|requestAnimationFrame|scrollTo\(|useAnimatedScrollHandler|useMotionValue|withFrameNanos',
 'css-rendering':r'@keyframes|transition:|animation:|animate-|RuntimeShader|Shader|Canvas|Skia|BlurView|backdrop-filter|graphicsLayer|ValueAnimator|ObjectAnimator|TransitionManager',
 'accessibility-motion':r'useReducedMotion|ReduceMotion|prefers-reduced-motion|MotionDurationScale|ANIMATOR_DURATION_SCALE',
}

def scan(p):
    cache=ROOT/f"projects/{p['id']}/references"
    manifest=ROOT/f"projects/{p['id']}/manifest.json"
    if manifest.exists() and (cache/'file-inventory.json').exists() and (cache/'animation-discovery.json').exists():
        old=json.loads(manifest.read_text(encoding='utf-8'))
        if old['commit']==p['commit']:
            return old['coverage']['scanned_text_files'], old['coverage']['discovery_hits']
    results=[]; files=[]
    for f in sorted(p['root'].rglob('*')):
        if not f.is_file() or '.git' in f.parts or f.suffix.lower() not in ['.ts','.tsx','.js','.jsx','.css','.scss','.kt','.xml','.java','.swift','.m','.mm','.h','.cpp','.c','.glsl','.frag','.vert']:
            continue
        path=f.relative_to(p['root']).as_posix()
        raw=f.read_bytes(); content=raw.decode('utf-8',errors='replace')
        files.append(dict(path=path,sha256=hashlib.sha256(raw).hexdigest()))
        for n,line in enumerate(content.splitlines(),1):
            cats=[k for k,v in SEARCH.items() if re.search(v,line)]
            if cats:
                results.append(dict(path=path,line=n,categories=cats,text=line.strip()[:350],
                    test_or_fixture=any(t in path.lower() for t in ['__tests__','/test/','/tests/','fixture','stories']),
                    status='discovered-not-individually-reviewed'))
    base=f"projects/{p['id']}/references"
    dump(base+'/animation-discovery.json',dict(scope='full snapshot supported text extensions; lexical hits are candidates, not confirmed animations',patterns=SEARCH,hits=results))
    dump(base+'/file-inventory.json',dict(files=files))
    return len(files),len(results)

def finish_project(p):
    base=f"projects/{p['id']}"
    p.setdefault('license','Apache-2.0' if p['id']=='mihon' else 'AGPL-3.0')
    license_text=text_file(p['root'],'LICENSE')
    write(base+'/references/UPSTREAM-LICENSE.txt',license_text)
    files,hits=scan(p)
    for name,(body,refs) in p['docs'].items():
        write(base+'/'+name, f"# {name.split('/')[-1].removesuffix('.md')}\n\n{body}\n\n## 来源与状态\n\nsource-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。\n\n{link_sources(refs)}")
    dump(base+'/design-language/tokens.json',dict(schema_version='1.0',project=p['id'],commit=p['commit'],tokens=p['tokens']))
    for slug,spec,mechanism in p['animations']:
        folder=base+'/animations/'+slug
        dump(folder+'/spec.json',spec)
        write(folder+'/README.md',f"# {spec['name']}\n\nID：`{spec['id']}` · source-verified · 原项目未运行\n\n{spec['effect']}\n\n适用：{spec['applicable']}\n\n不适用：{spec['not_applicable']}\n\n- [结构化规格](spec.json)\n- [原理、状态机与迁移](implementation.md)\n- [固定版本源码](source-reference.md)\n\n参数为 null 的字段不可补成框架默认数值。没有实录预览。")
        write(folder+'/implementation.md',f"# 实现原理\n\n{mechanism}\n\n## 生命周期与快速触发\n\n{spec['interruption']}\n\n## 框架无关行为\n\n输入：{spec['trigger']}\n\n状态从 `{json.dumps(spec['start_state'],ensure_ascii=False)}` 到 `{json.dumps(spec['end_state'],ensure_ascii=False)}`。\n\n以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。\n\n手势：{spec['gesture'] or '本实现没有直接手势轨道；通过状态驱动。'}\n\n## 无障碍\n\n{spec['accessibility']}\n\n## 性能（静态分析，无 FPS 或内存实测）\n\n{spec['performance']['notes']}\n\n## 迁移边界\n\n保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。\n\n{link_sources(spec['sources'])}")
        write(folder+'/source-reference.md',f"# 原始实现\n\n仓库：{p['repo']}\n\nCommit：`{p['commit']}`\n\n{link_sources(spec['sources'])}\n\n本目录没有整段复制业务实现。哈希与精确定位保存在 [source-map](../../references/source-map.json)。按源码链接阅读原始层；spec.json 与 implementation.md 为行为分析层；examples 若存在则为第三层。许可证与署名见 [LICENSE-NOTES](../../LICENSE-NOTES.md)。")
    for slug,spec in p['components']:
        folder=base+'/components/'+slug
        dump(folder+'/spec.json',spec)
        sections=[('用途',spec['purpose']),('结构',spec['structure']),('参数',spec['parameters']),('交互状态',spec['states']),('输入、输出与状态',spec['api']),('反馈与生命周期',spec['behavior']),('框架无关迁移',spec['migration']),('最小用法（说明性片段，未编译）','```\n'+spec['minimal_usage']+'\n```'),('限制',spec['not_applicable'])]
        write(folder+'/README.md',f"# {spec['name']}\n\n`{spec['id']}` · source-verified · runtime unverified\n\n"+'\n\n'.join('## '+k+'\n\n'+v for k,v in sections)+'\n\n## 源码\n\n'+link_sources(spec['sources']))
    dump(base+'/references/source-map.json',list(p['sources'].values()))
    manifest=dict(schema_version='1.0',id=p['id'],name=p['id'],description=p['overview'],repository=p['repo'],branch='main',commit=p['commit'],version=p['version'],analysis_date=DATE,platforms=p['platforms'],stack=p['stack'],source_directories=p['dirs'],source_snapshot=p['root'].relative_to(WORK).as_posix(),license=p['license'],coverage=dict(status='core-system-and-selected-high-value-resources',scanned_text_files=files,discovery_hits=hits,components=len(p['components']),animations=len(p['animations']),original_app_runtime=False),design_features=p['overview'],verification=['source-verified'],runtime_verified=False,not_portable=['业务状态容器、私有模块路径与平台导航不能整体复制','第三方组件的未追溯默认动效不能当作项目 Token'],backlog='BACKLOG.md')
    dump(base+'/manifest.json',manifest)
    links='\n'.join(f"- [{s['name']}](animations/{slug}/README.md)" for slug,s,_ in p['animations'])
    comps='\n'.join(f"- [{s['name']}](components/{slug}/README.md)" for slug,s in p['components'])
    write(base+'/README.md',f"# {p['id']}\n\n{p['overview']}\n\n分析版本：{p['version']} / main / `{p['commit']}`。{files} 个文本源文件参与全仓候选扫描；{hits} 条词法命中不等于 {hits} 个动画。\n\n## 阅读导航\n\n1. [设计语言](design-language/overview.md) → [Token](design-language/tokens.json) → [布局](design-language/layout.md)\n2. 按需选组件或动画，然后读取同目录 spec.json。\n3. [架构](architecture/overview.md) · [交互](interactions/overview.md) · [许可证](LICENSE-NOTES.md)\n4. [覆盖范围与待办](BACKLOG.md) · [来源索引](references/source-map.json)\n\n## 组件\n\n{comps}\n\n## 动画\n\n{links}\n\n## 完成边界\n\n核心资料可检索；原项目未构建、未运行、未录屏。完整候选清单在 references/animation-discovery.json；业务页面、依赖默认值和设备行为仍需后续深化。不要将“源码确认”理解为“运行效果确认”。")
    if p['id']=='mihon':
        legal='上游 LICENSE 为 Apache License 2.0。分发摘录/改编需保留版权、许可证和适用 NOTICE；修改文件须显著说明修改。Elevation.kt 明确带有 Android Open Source Project 2021 版权和 Apache 2.0 头，不能只署 Mihon。未发现根级 NOTICE 不代表依赖没有 NOTICE。'
    elif p['license']=='GPL-3.0':
        legal='上游 LICENSE 为 GNU General Public License version 3，README 同样标为 GPL-3.0；不是 AGPL。摘录和改编继续保留来源、修改说明及 GPL 许可，不能混用本库其他项目的 AGPL/Apache 标签。Linux 运行时、游戏图像、Valve/其他商标及子模块另有权利和许可证，本轮不分发这些内容。'
    else:
        legal='上游 LICENSE 为 GNU Affero General Public License v3。摘录或改编不因为放进知识库就变为宽松许可；分发、组合或网络交互引起的源码提供等义务须依完整许可证判断。本库不承诺“独立重写”标签自动排除衍生作品关系。商业复用按上游授权路径核实。'
    write(base+'/LICENSE-NOTES.md',f"# 来源与复用边界\n\n{p['repo']} @ `{p['commit']}`\n\n{legal}\n\n完整许可：[上游 LICENSE 原文](references/UPSTREAM-LICENSE.txt)。原始版权逐文件以固定版本源文件头及许可证为准；不替原作者授予商标、图标或第三方字体/图片权利。\n\n- 原始源码：保存在知识库之外的 source-repositories，未改动。\n- 分析文档与规格：本任务产出的总结；source-verified 与 inferred 按具体主张区分。\n- adapted 示例：即使减少了业务依赖，仍保留来源和对应上游许可。\n- original-reimplementation 示例：基于行为规格单独编写，明确与原框架/业务实现的差异。\n\n未搬运上游截图、商标、字体与媒体；assets/、preview/ 因无实录/授权整理需要而未创建。")
    return manifest

if __name__=='__main__':
    print('Run author.py to build research data and index.')
