import time


from selenium import webdriver
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://www.cleartrip.com/")
from_element = chrome.find_element_by_xpath(xpath="//input[@id='FromTag']")

key_board = ActionChains(driver=chrome)


key_board.move_to_element(to_element=from_element).click().pause(seconds=3).send_keys("tri").pause(seconds=3).send_keys(Key.ARROW_DOWN).pause(seconds=3).send_keys(Key.ARROW_DOWN)pause(seconds=3).send_keys(Key.ARROW_DOWN)key_board.move_to_element(to_element=from_element).click().pause(seconds=3).send_keys("tri").pause(seconds=3).send_keys(Key.ARROW_DOWN).pause(seconds=3).send_keys(Key.ARROW_DOWN).pause(seconds=3).send_keys(Key.ARROW_DOWN)


time.sleep(3)
chrome.quit()