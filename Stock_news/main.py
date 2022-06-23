import requests
from datetime import datetime, timedelta
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

twilio_account_sid = 'AC8e84a5a008e539fe7ec458896c94fb33'
twilio_auth_token = "40a2d3383acf2b2d5c9aa9c14932ee71"
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ.get("https_proxy")}

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "00AHJ55EWHEFJTNT"
news_api_key = "ab53b9fda19d4ca3a9c5227b73c22078"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}
news_params = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
}

stock_data = requests.get(STOCK_ENDPOINT, params=stock_params).json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])

day_before_data = data_list[1]
day_before_closing_price = float(day_before_data['4. close'])

difference = round(yesterday_closing_price - day_before_closing_price)
percentage_diff = (difference / day_before_closing_price) * 100
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"
if abs(percentage_diff) < 5:

    news = requests.get(NEWS_ENDPOINT, params=news_params).json()
    articles = news["articles"][:3]
    client = Client(twilio_account_sid, twilio_auth_token, http_client=proxy_client)
    for article in articles:
        message = client.messages \
            .create(
             body=f"{STOCK_NAME}:{up_down}{percentage_diff}%\n\n Headline: {article['title']}\n\nBrief:{article['description']}",
             from_='+16816411664',
             to='+254114339386'
            )

