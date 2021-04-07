import requests
import api

api_key = api.get_api()
weather_url = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 51.496979,
    "lon": 11.968803,
    "appid": api_key
}

response = requests.get(weather_url, params=weather_params)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]

need_umbrella = False
for hour_data in data_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        need_umbrella = True

if need_umbrella:
    print("You'll need an umbrella today ☔️")
else:
    print("You won't need an umbrella today ☀️")
