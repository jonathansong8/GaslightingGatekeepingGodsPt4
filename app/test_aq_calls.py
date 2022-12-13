import requests

def process(url):
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    response = response.json()
    response = response["results"]
    return response

#Returns a Dict of Country Codes Along with their Respective Names
all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
dict_countries = {}
for country in all_countries:
    code = country["code"]
    name = country["name"]
    dict_countries[code] = name
#Get Only the Keys, which are the country codes
countries = list(dict_countries.keys())


#returns parsed project (likely unusable atm)
''''
projects = process("https://api.openaq.org/v2/projects")
count = 0
dict_gases = {}
for entry in projects:
    print(entry["parameters"][0])
    param = entry["parameters"][0]["displayName"] #the dict is the only thing inside the list
    val = str(entry["parameters"][0]["average"]) + " " + entry["parameters"][0]["unit"]
    dict_gases[param] = val
    count += 1
#print(count)
#print(dict_gases)
'''

#get all locations available in the openaq api and their corresponding entry id (menu dropdown?) [name,country:unique id]
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
print(dict_locations)

def lookup(id):
    link = process("https://api.openaq.org/v2/latest/" + str(id) + "?location_id?limit=100&page=1&offset=0&sort=desc&radius=1000&order_by=lastUpdated&dumpRaw=false")
    if link[0]["location"] is None:
        return "Invalid Location"
    else:    
        name_location = link[0]["location"]
    temp = link[0]["measurements"]
    return temp
   
'''
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
'''
