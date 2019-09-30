import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="C:/Users/janhavi/PycharmProjects/script/input1.html")
#chrome.find_element_by_xpath(xpath="//input[@id='fname']").send_keys("sachin")
chrome.find_element_by_xpath(xpath="//a[text()=' click here ']").click()
time.sleep(3)
handles = chrome.window_handles
chrome.switch_to.window(handles[1])
chrome.find_element_by_xpath(xpath="//input[@id='mname']").send_keys("ramesh")
chrome.find_element_by_xpath(xpath="//a[text()=' click here ']").click()
time.sleep(3)
handles1 = chrome.window_handles
chrome.switch_to.window(handles1[2])
chrome.find_element_by_xpath(xpath="//input[@id='lname']").send_keys("tendulkar")
time.sleep(3)
chrome.switch_to.window(handles1[0])
chrome.find_element_by_xpath(xpath="//input[@id='fname']").send_keys("sachin")
time.sleep(3)
chrome.quit()
