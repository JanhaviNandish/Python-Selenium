import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://magento.com/")
links = chrome.find_elements_by_tag_name("a")
#links = chrome.find_elements(By.TAG_NAME, "a")
print(type(links))

no_of_links = len(links)
print("the no of link is:", no_of_links)
print("the link text name is:")
for element in links:
    print(element.text)
time.sleep(3)
chrome.close()