import smtplib, random
import pandas as pd
import datetime as dt

email ="type your email here"
password = "type your password here"
current_date = dt.datetime.now().date()

def sendmail(sendto, subject, message):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
      from_addr=email, 
      to_addrs=sendto, 
      msg=f"Subject:{subject}\n\n{message}"
      )

df = pd.read_csv('Day 32/birthdays.csv')

for index, row in df.iterrows():
  if row.month == current_date.month and row.day == current_date.day:
    send_to_name = row['name']
    send_to_email = row['email']
    with open(f'Day 32/letter_templates/letter_{random.randint(1,3)}.txt') as template:
      birthday_letter = template.read()
      birthday_letter = birthday_letter.replace('[NAME]', send_to_name)
    sendmail(send_to_email, 'Happy Birthday', birthday_letter)