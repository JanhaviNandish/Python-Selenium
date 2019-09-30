from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.get(url="https://account.magento.com/customer/account/create/")
chrome.find_element_by_id(id_="firstname").send_keys("Janhavi")
chrome.find_element_by_id(id_="lastname").send_keys("Nandish")
chrome.find_element_by_id(id_="email_address").send_keys("janhavinandish@gmail.com")
drop_down = chrome.find_element_by_id(id_="country")
s = Select(webelement=drop_down)
s.select_by_visible_text(text="India")
drop2 = chrome.find_element_by_id(id_="customer_company_type")
s2 = Select(webelement=drop2)
s2.select_by_value(value="development")

