import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.get(url="http://www.echoecho.com/javascript4.htm")
chrome.find_element_by_xpath(xpath="//input[@name='B3']").click()
prompt_box = chrome.switch_to.alert
prompt_box.send_keys("Happy")

time.sleep(3)
prompt_box.accept()
time.sleep(3)
chrome.quit()
