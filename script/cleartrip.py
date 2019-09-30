import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://www.cleartrip.com/")
round_trip = chrome.find_element_by_xpath(xpath="//input[@id='RoundTrip']")

return_date = chrome.find_elements_by_xpath(xpath="//input[@id='ReturnDate']")

if round_trip.is_selected() == True:
    print("Round trip already selected")
else:
    round_trip.click()

if return_date.is_displayed() == True:
    return_date.send_keys("Tue, 30 Apr, 2019")
else:
    print("ReturnDate is not visible")

time.sleep(3)
chrome.close()

