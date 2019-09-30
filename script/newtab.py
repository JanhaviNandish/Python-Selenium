import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")

chrome.maximize_window()
chrome.get(url="https://www.facebook.com/")
key_board = ActionChains(driver=chrome)
key_board.key_down(Keys.CONTROL).send_keys("t").pause(seconds=5).perform()
time.sleep(5)
chrome.close()