from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import math

url = "https://www.torontorentals.com/toronto/apartments?rent-min=300&rent-max=1000"

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.get(url)
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='r-viewport']/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/a[1]")