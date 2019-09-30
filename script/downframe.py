import time

from selenium import webdriver
from sympy import chebyshevt_root

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://www.seleniumhq.org/download/")
chrome.find_element_by_xpath(xpath="//a[text()='Javadoc']").click()
time.sleep(3)
chrome.switch_to.frame(chrome.find_element_by_xpath(xpath="//frame[@name='packageListFrame']"))
time.sleep(3)
chrome.find_element_by_xpath(xpath="//a[text()='com.thoughtworks.selenium']").click()
time.sleep(3)
chrome.switch_to.default_content()
time.sleep(3)
chrome.switch_to.frame(chrome.find_element_by_xpath(xpath="//frame[@name='packageFrame']"))
time.sleep(3)
chrome.find_element_by_xpath(xpath="//span[text()='Selenium']").click()
time.sleep(3)
chrome.switch_to.default_content()
time.sleep(3)
chrome.switch_to.frame(chrome.find_element_by_xpath(xpath="//frame[@name='classFrame']"))
time.sleep(3)
chrome.find_element_by_xpath(xpath="//a[text()='Overview']").click()
time.sleep(3)

chrome.quit()