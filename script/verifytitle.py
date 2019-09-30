from selenium import webdriver
e_title=input("enter the title:")
browser=webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
browser.maximize_window()
browser.get(url="http://www.gmail.com")
a_title=browser.title
print("The actual title is",a_title)
print("The expected title is",e_title)
if a_title.casefold()==e_title.casefold():
    print("PASS")
else:
    print("FAIL")
browser.close()
