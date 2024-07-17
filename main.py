import datetime as dt
import pandas as pd
import os, random, glob
import smtplib
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

today = dt.datetime.today()
month = int(today.strftime('%m'))
day = int(today.strftime('%d'))

df = pd.read_csv('birthdays.csv')
birthday_records = df.to_dict('records')

letters = [l for l in glob.glob("letter_templates/*") if os.path.isfile(l)]
random_letter = random.choice(letters)
name = "[NAME]"

for record in birthday_records:
    with open(random_letter) as letter:
        mail = letter.read()
        mail = mail.replace(name, record['name'])

    if record['month'] == month and record['day'] == day:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=record['email'],
                msg=f"Subject: Happy Birthday\n\n{mail}"
            )




