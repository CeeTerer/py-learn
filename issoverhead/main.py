import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -1.322380
MY_LONG = 36.706749
EMAIL = "terercynthiachep@gmail.com"
PASSWORD = "terer456"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def check_position():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 3
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 3
time_now = datetime.now().hour

# If the ISS is close to my current position
while True:
    time.sleep(60)
    if check_position() and (time_now <= sunrise or time_now >= sunset):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg="Subject:CHECK ISS\n\nThe ISS is above you now.")
            connection.close()

