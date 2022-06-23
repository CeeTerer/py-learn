import requests

GENDER = "female"
WEIGHT_KG = "50"
HEIGHT_CM = "154"
AGE = "20"

APP_ID = "2c967c26"
API_KEY ="b1b81b11b91f0b47f23b20f6e9f577ec"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)