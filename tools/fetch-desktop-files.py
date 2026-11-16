import urllib.request,pathlib,json,concurrent.futures
sha='c3263227592ad14313da2b4153bf88502c466454'
root=pathlib.Path('source-repositories/cherry-studio-review-files-'+sha[:12]);root.mkdir(exist_ok=True)
tree=json.loads(pathlib.Path('design-knowledge-base/projects/cherry-studio/references/repository-tree.json').read_text())['tree']
paths=[x['path'] for x in tree if x['type']=='blob' and (x['path'] in ['AGENTS.md','DESIGN.md','README.md','LICENSE','package.json'] or (x['path'].startswith(('packages/ui/src/styles/','packages/ui/src/components/primitives/','src/renderer/components/Sidebar/','src/renderer/components/chat/shell/','src/renderer/components/chat/motion/')) and '__tests__' not in x['path']) or x['path'] in ['src/renderer/assets/styles/animation.css','src/renderer/components/ThemeProvider.tsx','src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts','src/renderer/utils/motionActivity.ts','src/renderer/components/BrowserCursorAnimation.ts'])]
def fetch(p):
 try:
  b=urllib.request.urlopen('https://raw.githubusercontent.com/CherryHQ/cherry-studio/'+sha+'/'+p,timeout=35).read();f=root/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b)
 except Exception as e: print(p,str(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:list(ex.map(fetch,paths))
print('Fetched',len(paths),'selected files',flush=True)
