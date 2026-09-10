from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
required=['README.md','README.pdf','lab.yaml','prompt.md','starter/result.json','solution/result.json','evidence/checklist.md','evidence/checklist.pdf']
missing=[p for p in required if not (root/p).is_file() or (root/p).stat().st_size==0]
if missing:
    print('FAIL missing:', ', '.join(missing)); sys.exit(1)
data=json.loads((root/'solution/result.json').read_text())
fields=['lab_id','status','source_files','artifacts','decision','human_owner','acceptance']
bad=[k for k in fields if k not in data or data[k] in ('', [], None)]
if bad:
    print('FAIL fields:', ', '.join(bad)); sys.exit(1)
if data['lab_id']!=1 or data['status']!='PASS':
    print('FAIL identity/status'); sys.exit(1)
if not list((root/'mock-data').glob('*')):
    print('FAIL no mock data'); sys.exit(1)
print('PASS Lab 01: self-contained structure and reference artifact verified')
