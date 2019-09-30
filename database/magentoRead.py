
import mysql.connector
from selenium import webdriver

try:
    print("connecting to database")
    connection = mysql.connector.connect(host='localhost', database='magentodb', user='root', password='root')
    print("connected to database")
    cursor = connection.cursor()
    sql_select_query = "select * from magentotb"
    cursor.execute(sql_select_query)
    result_set = cursor.fetchall()
    print(result_set)

    chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver.exe")
    chrome.maximize_window()
    chrome.implicitly_wait(time_to_wait=20)
    chrome.get(url=result_set[0][0])
    #chrome.find_element_by_xpath("//a[text()='My Account']").click()
    chrome.find_element_by_xpath("//input[@id='email']").send_keys(result_set[0][1])
    chrome.find_element_by_xpath("//input[@id='pass']").send_keys(result_set[0][2])
    chrome.find_element_by_xpath("//button[@id='send2']").click()
    chrome.find_element_by_xpath("//a[text()='Log Out']").click()
    chrome.close()
except Exception as e:
    print("Exception occured",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close
        print("connection closed succesfully")