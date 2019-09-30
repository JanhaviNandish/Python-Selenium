
from selenium import webdriver
browser=webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
browser.maximize_window()
browser.get(url="http://www.gmail.com")
c_url=browser.current_url
print("current url is:",c_url)
browser.close()