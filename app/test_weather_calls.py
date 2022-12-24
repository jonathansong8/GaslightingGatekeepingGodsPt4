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

def add_to_dict(info,key,loc):
    if key not in info:
        info[key]=[]
    info[key].append(str(loc[key]))
def forecast(latitude,longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    original = process(url)
    forecast = {}
    other_links = {}
    for sub in original["properties"]:
        if "forecast" in sub:
            forecast[sub]=original["properties"][sub]
    
    info = {}
    general_forecast=forecast["forecast"] #this is a link
    curr_json = process(general_forecast)
    for i in curr_json["properties"]["periods"]:
        time = []
        add_to_dict(info, "isDaytime", i)
        add_to_dict(info, "temperature", i)
        add_to_dict(info, "temperatureUnit", i)
        add_to_dict(info, "windSpeed", i)
        add_to_dict(info, "windDirection", i)
        add_to_dict(info, "shortForecast", i)
        add_to_dict(info, "detailedForecast", i)
        
        """
        if "Temperature" not in info:
            info["Temperature"]=[]
        info["Temperature"].append(str(i["Temperature"]))
        if "isDaytime" not in info:
            info["isDaytime"]=[]
        info["isDaytime"].append(str(i["isDaytime"]))
        if "isDaytime" not in info:
            info["isDaytime"]=[]
        info["isDaytime"].append(str(i["isDaytime"]))
        time.append("isDaytime: "+str(i["isDaytime"]))
        time.append("Temperature: "+str(i["temperature"]))
        time.append("Temperature Unit: "+i["temperatureUnit"])
        time.append("Wind Speed: "+i["windSpeed"])
        time.append("Wind Direction: "+i["windDirection"])
        time.append("Short Forecast: "+i["shortForecast"])
        time.append("Detailed Forecast: "+i["detailedForecast"])
        """
    info = {i:"\n".join(info[i]) for i in info}
    for i in info:
        info[i]=info[i].split("\n")[0]
    return info
