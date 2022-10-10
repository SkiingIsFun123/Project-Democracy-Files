import requests
import yaml
import json

url = 'https://raw.githubusercontent.com/unitedstates/congress-legislators/main/legislators-current.yaml'
response = requests.get(url)
data = yaml.safe_load(response.text)
with open('legislators-current.json', 'w') as f:
    json.dump(data, f, indent=2)
