import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://magento.com/")

chrome.set_page_load_timeout(time_to_wait=5)
chrome.find_element_by_link_text("My Account").click()

time.sleep(5)
chrome.close()