import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_JT=F&f_WT=2%2C1&geoId=100710459&keywords"
           "=python%20developer&location=Kenya")
time.sleep(2)
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.send_keys(Keys.ENTER)
time.sleep(1)
username = driver.find_element(By.ID,"username")
username.send_keys("ceeterer@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("N/HLU:/ga2)qG5B")
login_button = driver.find_element(By.CLASS_NAME, "btn__primary--large ")
login_button.send_keys(Keys.ENTER)

jobs = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
jobs.click()

phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("PHONE")


submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")
submit_button.click()