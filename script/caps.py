import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")

chrome.maximize_window()
chrome.get(url="https://www.google.com/")
search_box = chrome.find_element_by_xpath(xpath="//input[@name='q']")

key_board = ActionChains(driver=chrome)
key_board.move_to_element(to_element=search_box).click().pause(seconds=3).key_down(Keys.SHIFT).send_keys("abcfortechnologytraining").pause(seconds=3).send_keys(Keys.ENTER).pause(seconds=3).perform()

time.sleep(3)
chrome.quit()