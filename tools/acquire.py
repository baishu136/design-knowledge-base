import urllib.request,json,concurrent.futures,zipfile,io,pathlib,hashlib
base=pathlib.Path(__file__).resolve().parents[2]
def fetch(repo):
 def get(url):
  return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'DesignKnowledgeResearch'}),timeout=180).read()
 meta=json.loads(get('https://api.github.com/repos/CherryHQ/'+repo))
 commit=json.loads(get('https://api.github.com/repos/CherryHQ/'+repo+'/commits/'+meta['default_branch']))
 sha=commit['sha']; dest=base/'source-repositories'/(repo+'-'+sha[:12])
 if dest.exists(): raise FileExistsError('Immutable snapshot already exists: '+str(dest))
 data=get('https://codeload.github.com/CherryHQ/'+repo+'/zip/'+sha)
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  for e in z.infolist():
   rel=pathlib.PurePosixPath(e.filename).parts[1:]
   if not rel: continue
   target=dest.joinpath(*rel).resolve()
   if not target.is_relative_to(dest.resolve()): raise ValueError('Unsafe archive path')
   if e.is_dir(): target.mkdir(parents=True,exist_ok=True)
   else:
    target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(z.read(e))
 record={'repository':meta['html_url'],'branch':meta['default_branch'],'commit':sha,'commit_date':commit['commit']['committer']['date'],'snapshot_path':str(dest.relative_to(base)).replace('\\','/'),'archive_sha256':hashlib.sha256(data).hexdigest(),'acquisition':'GitHub codeload immutable commit archive'}
 record_path=base/'design-knowledge-base'/'projects'/repo/'references'/('acquisition-'+sha[:12]+'.json')
 record_path.parent.mkdir(parents=True,exist_ok=True)
 record_path.write_text(json.dumps(record,indent=2),encoding='utf-8')
 print(json.dumps(record),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: list(ex.map(fetch,['cherry-studio-app','cherry-studio']))
