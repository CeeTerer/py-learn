import requests
import smtplib
from bs4 import BeautifulSoup

EMAIL = "terercynthiachep@gmail.com"
PASSWORD = "terer456"

# header = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/84.0.4147.125 Safari/537.36", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8" }

response = requests.get("https://www.jumia.co.ke/ultra-thin-wireless-mouse-2.4g-rechargeable-generic-mpg274617.html")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
price_text = soup.find(name="span", class_="-b")
price = price_text.get_text().split()
cost = float(price[1])
if cost < 500:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\nThe price for Generic Ultra-thin Wireless Mouse 2.4G "
                                f"Rechargeable is now available at KES {cost}.")
        connection.close()
