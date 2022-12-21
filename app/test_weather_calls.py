import requests

def process(url):
    response = requests.get(url)
    response = response.json()
    return response
def location(latitude,longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    original = process(url)
    city = original["properties"]["relativeLocation"]["properties"]["city"]
    state = original["properties"]["relativeLocation"]["properties"]["state"]
    return city,state
def forecast(latitude,longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    original = process(url)
    forecast = {}
    other_links = {}
    for sub in original["properties"]:
        if "forecast" in sub:
            forecast[sub]=original["properties"][sub]
    
    info = {}
    general_forecast=forecast["forecast"]
    curr_json = process(general_forecast)
    for i in curr_json["properties"]["periods"]:
        time = []
        time.append("Date: "+i["name"])
        time.append("isDaytime: "+str(i["isDaytime"]))
        time.append("Temperature: "+str(i["temperature"]))
        time.append("Temperature Unit: "+i["temperatureUnit"])
        time.append("Wind Speed: "+i["windSpeed"])
        time.append("Wind Direction: "+i["windDirection"])
        time.append("Short Forecast: "+i["shortForecast"])
        time.append("Detailed Forecast: "+i["detailedForecast"])
        info[i["number"]]="\n".join(time)
    return info
"""
def process(url):
    response = requests.get(url)
    response = response.json()
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
"""

