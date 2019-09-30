import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://account.magento.com/customer/account/create/")
submit_button = chrome.find_element_by_xpath(xpath="//button[@id='registerSubmit']")
print(submit_button.is_enabled())
time.sleep(5)
print(submit_button.is_enabled())
chrome.close()