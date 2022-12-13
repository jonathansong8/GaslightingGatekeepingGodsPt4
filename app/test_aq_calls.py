import requests

'''
url = "https://api.openaq.org/v2/locations?limit=1000&page=1&offset=0&sort=desc&radius=10000&country=US&order_by=lastUpdated&dumpRaw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
response = response.json()
#print(response["results"][0]["name"])

arr = []
for city in response["results"]:
    arr.append(city["name"])
print(arr)

params = "https://api.openaq.org/v2/parameters?limit=100&page=1&offset=0&sort=asc&order_by=id"
headers = {"accept": "application/json"}
response = requests.get(params, headers=headers)
response = response.json()

dict = {}
second = {}
for gas in response["results"]:
    dict[gas["name"]] = gas["id"]
    second[gas["description"]] = gas["preferredUnit"]
print(dict)
print(second)
'''

def process(url):
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    response = response.json()
    response = response["results"]
    return response

all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
dict_countries = {}
for country in all_countries:
    code = country["code"]
    name = country["name"]
    dict_countries[code] = name
countries = list(dict_countries.keys())

projects = process("https://api.openaq.org/v2/projects")
#print(projects[0])
count = 0
dict_gases = {}
for entry in projects:
    param = entry["parameters"][0]["displayName"] #the dict is the only thing inside the list
    val = str(entry["parameters"][0]["average"]) + " " + entry["parameters"][0]["unit"]
    dict_gases[param] = val
    count += 1
#print(dict_gases)

x = process("https://api.openaq.org/v2/locations")
dict_locations = {}
for entry in x:
    if entry["country"] is not None and entry["name"] is not None:
        name = entry["name"] + ", " + entry["country"]
    else:
        name = entry["name"]
    code = entry["id"]
    dict_locations[code] = name
ids = list(dict_locations.keys())

arr = []
for id in ids:
    y = process("https://api.openaq.org/v2/latest/" + str(id) + "?location_id?limit=100&page=1&offset=0&sort=desc&radius=1000&order_by=lastUpdated&dumpRaw=false")
    if y[0]["location"] is None:
        continue
    name = y[0]["location"]
    y = y[0]["measurements"]
    for any in y:
        key = any["parameter"]+", "+ any["unit"] + " in " + name
        print(key)
        print(any["value"])
        arr.append([key,any["value"]])

print(arr)


