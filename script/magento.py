import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://magento.com/")
chrome.find_element_by_link_text(link_text="My Account").click()
time.sleep(15)
#halting the program execution
chrome.find_element_by_id(id_="email").send_keys("nitinmanjunath1991@gmail.com")
chrome.find_element_by_id(id_="pass").send_keys("Welcome123")
chrome.find_element_by_id(id_="send2").click()
time.sleep(5)
chrome.find_element_by_link_text(link_text="Log Out")
chrome.close()

