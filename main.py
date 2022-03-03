import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()

login = os.getenv("login")
password = os.getenv("password")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")

