import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
from dotenv import load_dotenv
import time
load_dotenv()

login = os.getenv("login")
password = os.getenv("password")
path = "C:/Users/Łukasz/Git/Selenium Webdriver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")


class InstaFollower(Options, By):

    def __init__(self):
        Options.__init__(self)
        By.__init__(self)

        self.driver = selenium.webdriver.Chrome(executable_path=path, options=chrome_options)
        self.driver.get("https://www.instagram.com/")
        self.login()

    def login(self):

        self.driver.implicitly_wait(1)
        agreements = self.driver.find_element(By.CLASS_NAME, "HoLwm")
        agreements.click()
        login_box = self.driver.find_element(By.NAME, "username")
        login_box.send_keys("Kalitoczenko")
        password_box = self.driver.find_element(By.NAME, "password")
        password_box.send_keys("TD/iGbky_Mz94Cj")
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div")
        login_button.click()
        time.sleep(5)
        self.find_followers()

    def find_followers(self):

        self.driver.get("https://www.instagram.com/chefsteps/")




    # def follow(self):
    #
    #     pass
    #

InstaFollower()
