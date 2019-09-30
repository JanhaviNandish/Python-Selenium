import time

from selenium import webdriver
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://demo.guru99.com/test/simple_context_menu.html")
right_click = chrome.find_element_by_xpath(xpath="//span[text()='right click me']")
double_click = chrome.find_element_by_xpath(xpath="//button[text()='Double-Click Me To See Alert']")
mouse = ActionChains(driver=chrome)
mouse.context_click(on_element=right_click).perform()
mouse.double_click(on_element=double_click).perform()
time.sleep(3)
chrome.quit()