
import datetime as dt
import pandas as pd
import random as rd
import smtplib


today = dt.datetime.now()
birthday = False
birthday_user: str = ""
birthday_email: str = ""

df = pd.read_csv("birthdays.csv")

if int(df['month'].iloc[0]) == today.month and int(df['day'].iloc[0]) == today.day:
    birthday = True
    birthday_users = df['name']
    birthday_emails = df['email']

for i, j in zip(birthday_emails, birthday_users):
    print(i, j)



if birthday:
        
    for birthday_email, birthday_user in zip(birthday_emails, birthday_users):

        letter_no = rd.randint(1, 3)

        with open(f"letter_templates/letter_{letter_no}.txt", "r") as f:
            letter = f.read()

        letter = letter.replace("[NAME]", birthday_user)


        my_email = "" # <- example@email.com
        my_pass = "" # <- password
        try:
            with smtplib.SMTP(host = "smtp.gmail.com", port= 587) as conn:
                conn.starttls()
                conn.login(user= my_email,password= my_pass)
                conn.sendmail(
                    from_addr= my_email,
                    to_addrs= birthday_email,
                    msg = f"Subject:Happy Birthday {birthday_user}\n\n{letter}",
                )

        except Exception as e:
            print(e)
        else:
            print("message delivered succesfully . . .")

else:
    print("Today no birthday")

