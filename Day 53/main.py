from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

zillow_res = requests.get('https://appbrewery.github.io/Zillow-Clone/')
zillow_site = zillow_res.text

zillow_parse = BeautifulSoup(zillow_site, 'html.parser')

addresses = zillow_parse.select('address')
addresses = [address.getText().strip().replace('|', '') for address in addresses]

prices = zillow_parse.select('.PropertyCardWrapper__StyledPriceLine ')
prices = [price.getText()[:6] for price in prices]

links = zillow_parse.select('.property-card-link')
links = [ link.get('href') for link in links]

driver = webdriver.Firefox()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSe6y83Hig6K-KvVXCmVyWzxNnwtcnhKBiia428YPFgpg6zTOg/viewform?usp=sf_link')
time.sleep(.5)


for i in range(len(addresses)):
  address_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  price_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
  link_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
  submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

  address_field.send_keys(addresses[i])
  price_field.send_keys(prices[i])
  link_field.send_keys(links[i])

  submit.click()

  time.sleep(.5)
  next_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
  next_link.click()

driver.quit()