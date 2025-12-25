import requests
from datetime import datetime
import os

app_id = os.environ['App_id']
app_key = os.environ['App_key']
username = os.environ['Username']
password = os.environ['Password']
url = os.environ['Url']
sheety_url = os.environ['Sheety_url']
headers = {
    "Content-Type": "application/json",
    "x-app-id": app_id,
    "x-app-key" : app_key,
}
data = {
    "query": input("What exercise did you do today?\n"),
    "weight_kg": 68,
    "height_cm": 184,
    "age": 18,
    "gender": "male"
}
response = requests.post(url=url, headers=headers, json=data)
result = response.json()

exercise_name = result["exercises"][0]["name"]
duration_time = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

today = datetime.today()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

sheet_insert = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": duration_time,
            "calories": calories,
        }
}
response_yes = requests.post(url=sheety_url, json=sheet_insert, headers=headers, auth=(username, password))
print(response_yes.text)
print(response_yes.status_code)
