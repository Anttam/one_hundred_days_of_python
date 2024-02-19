import requests
import smtplib
import time 
import datetime as dt

MY_LAT = 39.952583         
MY_LNG = -75.165222

email = "type your email here"
password = "type your password here"

sun_parameters={
  'lat': MY_LAT,
  'lng': MY_LNG,
  'formatted':0
}

def close_to_iss():
  iss_res = requests.get(url='http://api.open-notify.org/iss-now.json')
  iss_res.raise_for_status()
  iss_pos = iss_res.json()['iss_position']
  if MY_LAT-5 <= float(iss_pos['latitude']) <= MY_LAT+5:
    if MY_LNG-5 <= float(iss_pos['longitude']) <= MY_LNG+5:
      return True
  return False

def is_dark_outside():
  current_hour = dt.datetime.now().hour
  sun_res = requests.get('https://api.sunrise-sunset.org/json', params=sun_parameters)
  sun_data = sun_res.json()
  sunrise = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
  sunset = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])
  if current_hour >= sunset or current_hour <= sunrise:
    return True
  return False

def sendmail( subject, message):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
      from_addr=email, 
      to_addrs=email, 
      msg=f"Subject:{subject}\n\n{message}"
      )
    
while True:
  if close_to_iss():
    if is_dark_outside():
      sendmail('Look outside!', 'The ISS is currently overhead. If it is clear, you should be able to see it.')
  time.sleep(60)