import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
chrome.maximize_window()
chrome.get(url="http://localhost:63342/script/input1.html?_ijt=eipq716qp37fcmnmtl65akm19c")