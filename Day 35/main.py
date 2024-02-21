import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

MY_LAT = 39.952583         
MY_LNG = -75.165222

weather_params = {
  'lat': MY_LAT,
  'lon': MY_LNG,
  'appid': api_key,
  'cnt': 4,
}

def sendmail( subject, message):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
      from_addr=email, 
      to_addrs=email, 
      msg=f"Subject:{subject}\n\n{message}"
      )

res = requests.get('https://api.openweathermap.org/data/2.5/weather', params=weather_params)
res.raise_for_status()
weather_data = res.json()

for data in weather_data['list']:
  if int(data['weather'][0]['id']) <= 700:
    sendmail('Precipitation today', 'you should bring an umbrella today, it is going to rain or snow.')
    break

