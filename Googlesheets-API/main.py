import requests as requests

API_ID = "2c967c26"
API_KEY = "b1b81b11b91f0b47f23b20f6e9f577ec"

# figure out how to print the exercise stats for a plain text input.

my_text = input("Tell me which exercise you did: ")
NUTRI_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
# headers={
# x-app-id
# x-app-key
# Content-Type: application/json
# }

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
exercise_params = {
    "query": my_text,
    # "gender": "female",
    # "weight_kg": 72.5,
    # "height_cm": 167.64,
    # "age": 30
}

response = requests.post(NUTRI_ENDPOINT, json=exercise_params, headers=header)
result = response.json()
print(result)
