from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.python.org/")
# values = driver.find_elements(By.TAG_NAME, "time")
# print(values)
event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events_list = {}
for n in range(len(event_times)):
    events_list[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
       }
print(events_list)
driver.quit()
