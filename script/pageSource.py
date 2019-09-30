from selenium import webdriver
browser= webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
browser.maximize_window()
browser.get(url="http://www.gmail.com")
source = browser.page_source
print("the source code is:",source)
browser.close()
