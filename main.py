##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

MY_EMAIL = "kemgafreestyler@gmail.com"
MY_PASSWORD = "fspchzbcoehvzypi"

today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = { (row["month"],row["day"]): row for (index,row) in data.iterrows() }

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birhtday!\n\n{contents}"
        )