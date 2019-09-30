import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
browser.maximize_window()
browser.get(url="http://www.facebook.com")

email = browser.find_element(By.CLASS_NAME,"inputtext")
email.send_keys("sachin@gmail.com")
time.sleep(5)

pwd = browser.find_element(By.CLASS_NAME,"inputtext")
email.send_keys("1234")

time.sleep(5)
browser.close()