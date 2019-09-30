import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
old_window_size = chrome.get_window_size()
print("the window size is:",old_window_size)

chrome.set_window_size(width=old_window_size['width']/2, height=old_window_size['height']/2)

new_window_size = chrome.get_window_size()
print("the window size is:",new_window_size)
time.sleep(3)
chrome.close()