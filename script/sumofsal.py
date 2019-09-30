import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver.exe")
chrome.maximize_window()
chrome.get(url="https://datatables.net/extensions/select/examples/initialisation/checkbox.html")
row_info = chrome.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
row_count =len(row_info)
for row in range(1,row_count+1):
    sal_info = chrome.find_element_by_xpath(By.XPATH, "//table[@id='example']/tbody/tr[" + str(row) + "]/td[6]")
    sal_string = sal_info.text
    sal_string = sal_string.replace('$', '').replace(',', '')
    sal_int = int(sal_string)
    total = total+sal_int
print("total salary is:",total)
time.sleep(3)
chrome.close()