
import time
from selenium import webdriver
browser=webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver_win32\chromedriver")
browser.maximize_window()
browser.get(url="http://www.gmail.com")
time.sleep(5)
browser.close()
