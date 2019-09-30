import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.get(url="http://www.echoecho.com/javascript4.htm")
chrome.find_element_by_xpath(xpath="//input[@name='B2']").click()
confirm_box = chrome.switch_to.alert
print(confirm_box.text)

time.sleep(3)
confirm_box.dismiss()
time.sleep(3)
chrome.quit()
