import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://www.facebook.com")
chrome.find_element_by_partial_link_text("acc").click()
time.sleep(5)
chrome.close()


