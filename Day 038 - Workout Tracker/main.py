import requests
from keys import application_key, application_id, user_age, user_gender, sheety_username, sheety_password
from datetime import datetime

APP_ID = application_id
APP_KEY = application_key

AGE = user_age
GENDER = user_gender

SHEETY_USERNAME = sheety_username
SHEETY_PASSWORD = sheety_password

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/962b24bb7e2ff538b3793888d9a20d99/myWorkouts/workouts"

query_text = input("What did you do today?")

nutri_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nutri_params = {
    "query": query_text,
    "gender": GENDER,
    "age": AGE
}

response = requests.post(nutri_endpoint, json=nutri_params, headers=nutri_header)
data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            sheety_username,
            sheety_password
        )
    )

    print(sheet_response.text)
