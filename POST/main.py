import datetime

import requests

pixela_end = "https://pixe.la/v1/users"
USERNAME = "terer"
TOKEN = "3uyhjgndAcoks6"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# create user
# response= requests.post(pixela_end, json=user_params)
# print(response.text)
# today = # datetime.datetime.now()
today = datetime.datetime(year=2022, month=3, day=31)
graph_endpoint = f"{pixela_end}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# create graph
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}
# post pixel
pixel_end = f"{pixela_end}/{USERNAME}/graphs/graph1"
# response = requests.post(url=pixel_end,json=pixel_params,headers=headers)
# print(response.text)
update_end = f"{pixela_end}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "2",
}
response = requests.put(url=update_end,json=update_params,headers=headers)
print(response.text)