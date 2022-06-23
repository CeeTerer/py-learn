from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import math
SIMILAR_ACCOUNT = "ntvkenya"


class InstaFollower:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
        self.driver = webdriver.Chrome(service=Service(self.chrome_driver_path), options=self.chrome_options)
        self.driver.get("https://www.instagram.com/cynthia_ter_/")

    def login(self):
        # time.sleep(3)
        # login_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button")
        # login_button.click()

        time.sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("CT1_1234")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123564")

        login = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
        login.click()

        time.sleep(3)
        dont_save_login = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button")
        dont_save_login.click()

    def find_followers(self):
        time.sleep(3)
        followers= self.driver.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        original_window = self.driver.current_window_handle

        time.sleep(3)
        scroll = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]")
        time.sleep(3)

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                wait = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(window_handle))
                time.sleep(3)
        # scroll_height = 0

            while True:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
                time.sleep(3)
                names = self.driver.find_elements(By.CSS_SELECTOR, "uu6c,a")
                for name in names:
                    name_txt = name.text
                    print(name_txt)





    def follow(self):
        pass


instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()