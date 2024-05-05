import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = "54"
HEIGHT_CM = "1.71"
AGE = "36"
application_ID = "" # I deleted the application_ID itself before posting.
application_key = "" # I deleted the application_key itself before posting.
end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    'x-app-id': application_ID,
    'x-app-key': application_key
  }
response = requests.post(url=end_point, headers=headers, json=params)
data = response.json()
TOKEN = "" # I deleted the TOKEN itself before posting.
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(end_point, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)