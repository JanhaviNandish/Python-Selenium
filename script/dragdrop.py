import time

from selenium import webdriver
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
drag_element = chrome.find_element_by_xpath(xpath="//div[@id='box6']")
drop_element = chrome.find_element_by_xpath(xpath="//div[@id='box106']")
mouse = ActionChains(driver=chrome)
mouse.drag_and_drop(source=drag_element,target=drop_element).perform()
time.sleep(3)
chrome.quit()
