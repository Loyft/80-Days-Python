import datetime as dt
import pandas as pd
from random import choice
import smtplib

MY_EMAIL = "mymail@gmail.com"
MY_PASSWORD = "mypassword"

current_date = dt.datetime.now()
current_day = (current_date.month, current_date.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if (current_date.month, current_date.day) in birthday_dict:
    birthday_person = birthday_dict[current_day]
    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = choice(letter_list)
    file_path = f"letter_templates/{letter}"
    with open(file_path) as letter_file:
        letter_data = letter_file.read()
        letter_data = letter_data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_data}"
        )
