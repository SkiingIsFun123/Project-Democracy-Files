import requests
import yaml
import json

url = 'https://raw.githubusercontent.com/unitedstates/congress-legislators/main/legislators-current.yaml'
response = requests.get(url)
data = yaml.safe_load(response.text)
with open('legislators-current.json', 'w') as f:
    json.dump(data, f, indent=2)

name = "Mike Levin"
def getPhoneNumber(name):
    with open('legislators-current.json', 'r') as f:
        data = json.load(f)
        for i in data:
            if i['name']['official_full'] == name:
                return i['terms'][0]['phone']

def getIds(name):
    with open('candidates.json', 'r') as f:
        data = json.load(f)
        for candidateName in data:
            if candidateName == name:
                feccandid = data[candidateName][3]
                cid = data[candidateName][0]
                return feccandid, cid
            else:
                pass

print(getPhoneNumber(name))
print(getIds(name)[0])
print(getIds(name)[1])
