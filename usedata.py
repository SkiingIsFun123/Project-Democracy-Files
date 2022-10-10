import requests
import yaml
import json
import datetime

#check if theres a json file named today's date already
# if not, create one
today = datetime.date.today()
filename = today.strftime('%Y-%m-%d') + '.json'

def accessJSONFile():
    try:
        with open(filename, 'r') as f:
            pass
    except:
        url = 'https://raw.githubusercontent.com/unitedstates/congress-legislators/main/legislators-current.yaml'
        response = requests.get(url)
        data = yaml.safe_load(response.text)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

accessJSONFile()

name = "Nancy Pelosi"
def getData(name):
    with open(filename, 'r') as f:
        data = json.load(f)
        for i in data:
            if i['name']['official_full'] == name:
                try:
                    phonenumber =  i['terms'][0]['phone']
                except:
                    phonenumber = "N/A"
                try:
                    opensecrets = i['id']['opensecrets']
                except:
                    phonenumber = "N/A"
                try:
                    address = i['terms'][0]['address']
                except:
                    address = "N/A"
                return phonenumber, opensecrets, address

def getFromCandidates(name):
    with open('candidates.json', 'r') as f:
        data = json.load(f)
        for candidateName in data:
            if candidateName == name:
                feccandid = data[candidateName][3]
                return feccandid
            else:
                pass

candidateData = getFromCandidates(name)
legislatorData = getData(name)

print(candidateData)
print(legislatorData[0])
print(legislatorData[1])
print(legislatorData[2])

def getOrganizations(cid):
    url = 'https://www.opensecrets.org/api/?method=candContrib&cid=' + cid + '&cycle=2022&apikey=c5d1d02a93919b2845a095e52c2af67a&output=json'
    response = requests.get(url)
    data = response.text
    jsonData = json.loads(data)
    orgs = {}
    for i in jsonData['response']['contributors']['contributor']:
        org = i['@attributes']['org_name']
        total = i['@attributes']['total']
        orgs[org] = total
    return orgs

def getSectors(cid):
    url = 'https://www.opensecrets.org/api/?method=candSector&cid=' + cid + '&cycle=2022&apikey=c5d1d02a93919b2845a095e52c2af67a&output=json'
    response = requests.get(url)
    data = response.text
    jsonData = json.loads(data)
    sectors = {}
    for i in jsonData['response']['sectors']['sector']:
        sector = i['@attributes']['sector_name']
        total = i['@attributes']['total']
        sectors[sector] = total
    return sectors

candidateID = legislatorData[1]

topsupporters = getOrganizations(candidateID)
print(topsupporters)

topsectors = getSectors(candidateID)
print(topsectors)
