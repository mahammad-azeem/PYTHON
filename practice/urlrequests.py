from pathlib import Path
import requests
import json

url = "http://localhost:8080/job/terraform-test/api/json?pretty=true"
#r = requests.get(url)

#data = json.dumps(r.json())
#if r.status_code == 200:
#    print(r.json())
#else:
#    print(f"Request failed with status : {r.status_code}")

session = requests.Session()
session.auth = ('admin', 'admin')
r = session.get(url)
#data = r.text
Path("url.json").write_text(r.text)
parse = json.loads(r.text)

print(parse)
print(parse['name'])

#with open("url.json", 'r') as file:
#    print(file.read())