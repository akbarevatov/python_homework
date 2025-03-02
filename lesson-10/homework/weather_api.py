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
    print(f"Daily information:")
    print(f"Summary: {data["daily"][0]["summary"]}")
    print(f"Temperature (day): {round(float(data["daily"][0]["temp"]["day"])-273.15,1)} °C")
    print(f"Temperature (night): {round(float(data["daily"][0]["temp"]["night"])-273.15,1)} °C")
    print(f"Humidity: {data["daily"][0]["humidity"]} %")
    print(f"Wind speed: {data["daily"][0]["wind_speed"]} m/s")
else:
    print(f"Error: {response.status_code}")