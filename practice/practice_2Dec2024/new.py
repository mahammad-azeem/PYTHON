from pathlib import Path
import json

data = Path('series.json').read_text()
f = json.loads(data)
json.dumps(Path('write.json').write_text(data))
#print(Path('write.json').read_text())
print(f[0]['name'])