import hashlib, json, sys
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else 'mock-data/approved-draft.json')
data=json.loads(p.read_text())
canonical=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
print(hashlib.sha256(canonical).hexdigest())
