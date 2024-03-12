from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import dotenv
import time

dotenv.load_dotenv()

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

def abort_application():
  driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss").click()
  time.sleep(2)
  driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1].click()

driver = webdriver.Firefox()

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3753054505&f_AL=true&f_JT=F&f_WT=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')

driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(EMAIL)
driver.find_element(By.XPATH,'//*[@id="password"]' ).send_keys(PASSWORD)
driver.find_element(By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
time.sleep(2)

input("Press Enter when you have solved the Captcha")

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
  try:
    apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button").click()
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button").click()
    time.sleep(2)
  except NoSuchElementException:
    abort_application()
    print("No application button, skipped.")
    continue
