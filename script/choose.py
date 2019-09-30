import os
import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="C:/Users/janhavi/PycharmProjects/script/fileInput.html")
chrome.find_element_by_xpath(xpath="//input[@id='fileinput']").click()

time.sleep(3)
#to execute .exe file
#autoit file executed by python interpreter
os.system("F:\SeleniumComponents\file.exe")
time.sleep(3)
chrome.find_element_by_xpath(xpath="//input[@id='submit']")
time.sleep(3)
chrome.quit()
