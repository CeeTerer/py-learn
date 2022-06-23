import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as data:
    quotes = data.readlines()
    random_quote = random.choice(quotes)

    if weekday == 3:
        my_email = "cynthiachepterer@yahoo.com"
        password = "chpdeytmffmobzyt"
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="terercynthiachep@gmail.com",
                                msg=f"subject:Daily Quote\n\n{random_quote}")

