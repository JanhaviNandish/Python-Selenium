import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://magento.com/")
chrome.find_element_by_link_text(link_text="My Account").click()
time.sleep(5)
chrome.back()
time.sleep(3)
chrome.refresh()
time.sleep(3)

chrome.forward()
chrome.close()

