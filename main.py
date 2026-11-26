# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import os, pandas, smtplib, random, datetime as dt

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

for (index, row) in data.iterrows():
    if today == (row["month"], row["day"]):
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as letter:
            contents = letter.read()
            contents = contents.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
            
