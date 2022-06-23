import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ.get("https_proxy")}
api_key = os.environ.get("WEATHER_API_KEY")

account_sid = 'AC8e84a5a008e539fe7ec458896c94fb33'
auth_token = os.environ.get('WEATHER_AUTH')
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": -1.292066,
    "lon": 36.821945,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

weather = requests.get(OWM_ENDPOINT, params=weather_params)

weather_data = weather.json()

weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="Carry an umbrella",
        from_='+16816411664',
        to='+254114339386'
    )

    print(message.status)