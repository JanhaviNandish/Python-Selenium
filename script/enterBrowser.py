from selenium import webdriver
import time
def activity(browser1):
    browser1.maximize_window()
    browser1.get(url="http://www.gmail.com")
    print("Title is:",browser1.title)
    print("current url is:",browser1.current_url)
    time.sleep(5)
    browser1.close()

browser=input("enter the browser")
if browser=='chrome':
    chrome=webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
    activity(chrome)
else:
    ie=webdriver.Ie(executable_path="F:\SeleniumComponents\IEDriverServer")
    activity(IE)

