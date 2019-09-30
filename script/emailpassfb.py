import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
browser.maximize_window()
browser.get(url="http://www.facebook.com")

email = browser.find_element_by_name("email")
email.send_keys("sachin@gmail.com")
pwd = browser.find_element_by_name("pass")
pwd.send_keys("welcome123")


time.sleep(5)
browser.close()