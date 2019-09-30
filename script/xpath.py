import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()

chrome.get(url="C:\\Users\\janhavi\\PycharmProjects\\script\\sample.html")
chrome.find_element_by_xpath(xpath="/html/body/center/input[1]").send_keys("janhavi@gmail.com")

time.sleep(3)
chrome.find_element_by_xpath(xpath="/html/body/center/input[2]").send_keys("janvi")
time.sleep(3)
chrome.close()