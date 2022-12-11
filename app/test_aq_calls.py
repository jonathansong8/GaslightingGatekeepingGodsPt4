import requests

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

