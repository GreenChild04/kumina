from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils.cmdUtils.userKeyUtils import UserKeyUtils
import os


def run():
    uku = UserKeyUtils
    hd = os.getcwd()

    PATH = os.path.join(hd, 'chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=0")
    driver = webdriver.Chrome(PATH, chrome_options=options)
    driver.maximize_window()
    driver.get('https://www.youtube.com')

    driver.close()
    input()
