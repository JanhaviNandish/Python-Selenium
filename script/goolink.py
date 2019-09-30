import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://google.com/")
links = chrome.find_elements_by_tag_name("a")
#links = chrome.find_elements(By.TAG_NAME, "a")
print("the link text name is:")

for element in links:
    link_text_name = element.text
    print(link_text_name)
print("links count",len(links))

time.sleep(3)
chrome.close()