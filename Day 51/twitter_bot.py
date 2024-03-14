from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import dotenv
import os

dotenv.load_dotenv()

PROMISE_UP = 10
PROMISE_DOWN = 150
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

class InternetSpeedTwitterBot:
  def __init__(self):
    self.driver = webdriver.Firefox()
    self.up = 0
    self.down = 0

  def get_internet_speed(self):
    self.driver.get('https://www.speedtest.net/')
    time.sleep(5)
    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
    time.sleep(50)
    self.down = float(self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
    self.up = float(self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
    if self.down < PROMISE_DOWN or self.up < PROMISE_UP:
      self.tweet_at_provider()


  def tweet_at_provider(self):
    self.driver.get("https://twitter.com/login")

    time.sleep(2)
    email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    time.sleep(2)
    password.send_keys(Keys.ENTER)

    time.sleep(5)
    tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

    tweet = f"Hey @comcast, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}up?"

    tweet_compose.send_keys(tweet)
    time.sleep(3)

    self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()

    self.driver.quit()
   