import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()

chrome.get(url="https://account.magento.com/customer/account/create/")

#locate drop down element using any locator
drop_down = chrome.find_element_by_id(id_="customer_company_type")

#crating object for Select class and pass drop down reference
s = Select(webelement=drop_down)

#select the option using index
s.select_by_index(index=4)
time.sleep(5)

#select the option using value
s.select_by_value(value="analyst_media")
time.sleep(5)

#select the option using the text
s.select_by_visible_text(text="Develops Magento extensions")
time.sleep(5)

chrome.close()