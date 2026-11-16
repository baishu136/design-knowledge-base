"""Small, dependency-free catalog query. Does not load source/token/discovery payloads."""
from pathlib import Path
import argparse, json, sys
sys.stdout.reconfigure(encoding='utf-8')
p=argparse.ArgumentParser()
p.add_argument('query', nargs='?', default='')
p.add_argument('--platform',default='')
p.add_argument('--project',default='')
p.add_argument('--type',default='')
p.add_argument('--limit',type=int,default=8)
a=p.parse_args()
catalog=json.loads((Path(__file__).resolve().parents[1]/'CATALOG.json').read_text(encoding='utf-8'))
matches=[]
for r in catalog['resources']:
    if a.platform and a.platform.lower() not in [v.lower() for v in r['platforms']]:continue
    if a.project and a.project!=r['project']:continue
    if a.type and a.type!=r['resource_type']:continue
    hay=' '.join([r['id'],r['name'],r['description'],*r['keywords']]).lower()
    if not all(t in hay for t in a.query.lower().split()):continue
    matches.append({k:r[k] for k in ['id','name','doc_path','spec_path','verification']})
print(json.dumps(matches[:max(0,a.limit)],ensure_ascii=False,indent=2))
