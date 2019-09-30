import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.get(url="http://www.echoecho.com/javascript4.htm")
chrome.find_element_by_xpath(xpath="//input[@name='B1']").click()
alert_box = chrome.switch_to.alert
print(alert_box.text)

time.sleep(3)
alert_box.accept()
time.sleep(3)
chrome.quit()
