from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://secure-retreat-92358.herokuapp.com/")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# #
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Cynthia")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Terer")

email = driver.find_element(By.NAME, "email")
email.send_keys("cynthiachep8@gmail.com")

enter_button = driver.find_element(By.CSS_SELECTOR, "form button")
enter_button.click()

