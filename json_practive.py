import json
from pathlib import Path

#data = json.loads("Series.json")
data = Path("series.json").read_text()
series = json.loads(data)
print(series[1]["name"])