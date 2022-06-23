from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_argument("--disable-popup-blocking")
chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path),options=chrome_option)
driver.get("https://twitter.com")
sign_in = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")
# My_twitter =
# Password =//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div