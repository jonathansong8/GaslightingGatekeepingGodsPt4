import requests

def process(url):
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    response = response.json()
    response = response["results"]
    return response

#Returns a Dict of Country Codes Along with their Respective Names
'''
all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
dict_countries = {}
for country in all_countries:
    code = country["code"]
    name = country["name"]
    dict_countries[code] = name
#Get Only the Keys, which are the country codes
countries = list(dict_countries.keys())
'''
#gets all cities associated with a country
def get__all_cities(country_name):
    cities = process("https://api.openaq.org/v2/cities?limit=100000&page=1&offset=0&sort=asc&country_id=" + country_name + "&order_by=city")
    a = []
    for city in cities:
        if not city["city"].isnumeric() and city["city"] != "unused" and city["city"] != "N/A":
            a.append(city["city"])
    return a


def find_city(city_name):
    x = process("https://api.openaq.org/v2/locations?limit=1000&page=1&offset=0&sort=desc&city=" + city_name + "&order_by=lastUpdated&dumpRaw=false")
    for loc in x:
        if loc["city"] == city_name and loc["id"]:
            return loc["id"]
    return "Not Found"


def lookup_by_city_id(id):
    link = process("https://api.openaq.org/v2/latest/" + str(id) + "?location_id?limit=100&page=1&offset=0&sort=desc&radius=1000&order_by=lastUpdated&dumpRaw=false")
    if link[0]["location"] is None:
        return "Invalid Location"
    else:
        name_location = link[0]["location"]
    temp = link[0]["measurements"]
    return temp

def lookup_by_city_name(code):
    link = process( "https://api.openaq.org/v2/latest?limit=100&page=1&offset=0&sort=desc&radius=1000&city=" + code + "&order_by=lastUpdated&dumpRaw=false")
    if link[0]["location"] is None:
        return "Invalid Location"
    else:
        name_location = link[0]["location"]
    temp = link[0]["measurements"]
    result = {}
    for entry in temp:
        key = entry["parameter"] + "(" + entry["unit"] + ")"
        value = entry["value"]
        result[key] = value
    #print(code + ", " + link[0]["country"])
    return result

def parse_measurements(city_id):
    result = {}
    for entry in city_id:
        key = entry["parameter"] + " (" + entry["unit"] + ")"
        value = entry["value"]
        result[key] = value
    return result

#from every city in every country, get a list of all air quality values
'''
arr_of_cities = []
for country in countries:
    arr_of_cities.append(get__all_cities(country))
for city_arr in arr_of_cities:
    for curr in city_arr:
        print(lookup_by_city_name(curr))
'''

#get all locations available in the openaq api and their corresponding entry id (menu dropdown?) [name,country:unique id]

'''
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
#print(dict_locations)
'''

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