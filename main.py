import selenium
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import os
import time
load_dotenv()

login = os.getenv("login")
password = os.getenv("password")
path = "C:/Users/Łukasz/Git/Selenium Webdriver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")


class InstaFollower(By, WebDriverWait):

    def __init__(self):
        By.__init__(self)
        self.driver = selenium.webdriver.Chrome(executable_path=path, options=chrome_options)
        WebDriverWait.__init__(self, self.driver, 2)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.instagram.com/")
        self.login()

    def login(self):

        agreements = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "HoLwm")))
        agreements.click()
        login_box = self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "username")))
        login_box.send_keys("Kalitoczenko")
        password_box = self.driver.find_element(By.NAME, "password")
        password_box.send_keys("TD/iGbky_Mz94Cj")
        login_button = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div")))
        login_button.click()
        time.sleep(5)
        self.driver.get("https://www.instagram.com/chefsteps/")
        popup = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                             "//*[@id='react-root']/section/main/"
                                                                             "div/header/section/ul/li[2]/a/div")))
        popup.click()
        self.follow(start_point=0, counter=0)

    def scroll_down(self):

        box = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "isgrP")))
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight", box)
        print("scrolldown")

    def follow(self, start_point, counter):
        buttons_class = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "PZuss")))
        buttons = buttons_class.find_elements(By.CSS_SELECTOR, "button")
        for i in range(start_point, len(buttons)):
            counter += 1
            try:
                time.sleep(5)
                buttons[i].click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()
                time.sleep(5)
                buttons[i].click()
            finally:
                pass

        self.scroll_down()
        time.sleep(1)
        start_point = counter
        self.follow(start_point, counter)


InstaFollower()
