import requests
import json
from cities import capital_cities
api_key = "b4cd273165d562113330e111b114c15a"
base_url = "https://api.openweathermap.org/data/3.0/onecall"



city = input("Enter a capital city: ").lower()
params = {
    "lat": capital_cities[city.capitalize()]["lat"],
    "lon": capital_cities[city.capitalize()]["lon"],
    "appid": api_key
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    
else:
    raise Exception(response.status_code)

print(f"Daily information:")
print(f"Summary: {data["daily"][0]["summary"]}")
