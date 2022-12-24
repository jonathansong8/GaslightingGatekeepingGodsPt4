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

def find_country_of(city_name):
    x = process("https://api.openaq.org/v2/locations?limit=1000&page=1&offset=0&sort=desc&city=" + city_name + "&order_by=lastUpdated&dumpRaw=false")
    for loc in x:
        if loc["city"] == city_name:
            temp = loc["country"]
    all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
    for country in all_countries:
        if country["code"] == temp:
            return country["name"].capitalize()
    return "Not Found"


def lookup_by_city_id(id):
    link = process("https://api.openaq.org/v2/latest/" + str(id) + "?location_id?limit=100&page=1&offset=0&sort=desc&radius=1000&order_by=lastUpdated&dumpRaw=false")
    if link[0]["location"] is None:
        return "Invalid Location"
    else:
        name_location = link[0]["location"]
    temp = link[0]["measurements"]
    return temp

def lookup_by_city_name(name):
    link = process( "https://api.openaq.org/v2/latest?limit=100&page=1&offset=0&sort=desc&radius=1000&city=" + name + "&order_by=lastUpdated&dumpRaw=false")
    name_location = link[0]["location"]
    try:
        temp = link[1]["measurements"]
    except:
        temp = link[0]["measurements"]
    result = {}
    for entry in temp:
        key = entry["parameter"] + " (Last Updated On: " + entry["lastUpdated"][:10] + ")"
        value = str(entry["value"]) + " " + entry["unit"] 
        result[key] = value
    #print(code + ", " + link[0]["country"])
    return result

def lookup_city_coords(name):
    link = process("https://api.openaq.org/v2/latest?limit=100&page=1&offset=0&sort=desc&radius=1000&country=US&city=" + name + "&order_by=lastUpdated&dumpRaw=false")
    try:
        temp = link[0]["coordinates"]
    except:
        temp = "Manual Intervention Required"
    arr = []
    for i in temp.values():
        arr.append(round(i,2))
    return arr

def parse_measurements(city_id):
    result = {}
    for entry in city_id:
        key = entry["parameter"] + " " + entry["unit"] 
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