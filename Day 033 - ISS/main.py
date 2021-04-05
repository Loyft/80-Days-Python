import requests
from datetime import datetime

MY_LAT = 51.339695
My_LONG = 12.373075


def get_iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    is_near = False
    if MY_LAT + 5 < latitude < MY_LAT - 5:
        if My_LONG + 5 < longitude < My_LONG - 5:
            is_near = True

    return is_near


def get_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": My_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise = int(sunrise.split("T")[1].split(":")[0])
    sunset = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    is_dark = False
    if sunrise < hour_now > sunset:
        is_dark = True

    return is_dark


if get_iss_pos():
    if get_nighttime():
        print("iss above")
    else:
        print("is near but not nightitme")
else:
    print("is not near")
