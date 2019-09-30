import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="C:/Users/janhavi/PycharmProjects/script/input1.html")
chrome.find_element_by_xpath(xpath="//input[@id='fname']").send_keys("ramesh")
time.sleep(3)
chrome.switch_to.frame(0)

chrome.find_element_by_xpath(xpath="//input[@id='lname']").send_keys("tendulkar")
time.sleep(3)
chrome.switch_to.default_content()

chrome.find_element_by_xpath(xpath="//input[@id='fname']").clear()
time.sleep(3)
chrome.find_element_by_xpath(xpath="//input[@id='fname']").send_keys("sachin")
time.sleep(3)
chrome.quit()

