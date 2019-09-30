import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://magento.com/")
links = chrome.find_elements_by_tag_name("a")
#links = chrome.find_elements(By.TAG_NAME, "a")
print("the link text name is:")

for element in links:
    link_text_name = element.text
    print(link_text_name)

    if link_text_name == 'My Account':
        element.click()
        break
time.sleep(3)
chrome.close()