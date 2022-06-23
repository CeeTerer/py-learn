import random, smtplib,datetime,pandas
date = datetime.datetime.now()
today_month = date.month
today_day = date.day
EMAIL = "terercynthiachep@gmail.com"
PASSWORD = "terer456"
data = pandas.read_csv("birthdays.csv")
today = (today_month, today_day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")
        connection.close()




