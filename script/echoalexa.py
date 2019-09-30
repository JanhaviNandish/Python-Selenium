import time

from selenium import webdriver
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="https://www.amazon.in/")
shop_by = chrome.find_element_by_xpath(xpath="//span[text()='Shop by']")
echo_alexa = chrome.find_element_by_xpath(xpath="//span[text()='Echo & Alexa']")
echo_dot = chrome.find_element_by_xpath(xpath="//span[text()='All-new Echo Dot']")
mouse = ActionChains(driver=chrome)
#time.sleep(3)
#mouse.move_to_element(to_element=shop_by).perform()
#time.sleep(3)
#mouse.move_to_element(to_element=echo_alexa).perform()
#time.sleep(3)
#mouse.move_to_element(to_element=echo_dot).click().perform()

mouse.move_to_element(to_element=shop_by).pause(seconds=3).move_to_element(to_element=echo_alexa).pause(seconds=3).move_to_element(to_element=echo_dot).pause(seconds=3).click().perform()
time.sleep(3)
chrome.quit()