import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")

chrome.maximize_window()
chrome.get(url="https://www.facebook.com/")
chrome.find_element_by_xpath(xpath="//input[@id='email']").send_keys("sachin@gmail.com")

key_board = ActionChains(driver=chrome)
key_board.send_keys(Keys.TAB).send_keys("tendulkar").perform()
time.sleep(3)
chrome.close()
