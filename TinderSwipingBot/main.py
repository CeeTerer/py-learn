import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_argument("--disable-popup-blocking")
chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path),options=chrome_option)
driver.get("https://tinder.com/app/recs")

# login = driver.find_element(By.XPATH, "//*[@id='c849239686']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
# # login.click()
# facebook_login = driver.find_element(By.XPATH,"//*[@id='c-879141390']/div/div/div[1]/div/div/div[3]/span/div[2]/button")



