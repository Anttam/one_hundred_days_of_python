from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import dotenv
import os

dotenv.load_dotenv()

FB_EMAIL = os.environ.get('EMAIL')
FB_PASSWORD = os.environ.get('PASSWORD')

driver = webdriver.Firefox()

driver.get("http://www.tinder.com")

sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()

sleep(2)

driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)

driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()

driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

for n in range(100):

    sleep(1)

    try:
       driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
      
    except ElementClickInterceptedException:
        try:
           driver.find_element_by_css_selector(".itsAMatch a").click()
          
        except NoSuchElementException:
            sleep(2)

driver.quit()