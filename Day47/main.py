import requests
from bs4 import BeautifulSoup
import smtplib
import dotenv
import os

dotenv.load_dotenv()
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-US;q=0.9,en;q=0.8"
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

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float <= 99.99:
    sendmail('Lower Price On Instant Pot', f'The instant pot has a new lower price of ${price_as_float}. you can purchase it here: \n\n {url}')