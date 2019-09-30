from selenium import webdriver
browser= webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver")
browser.maximize_window()
browser.get(url="http://www.gmail.com")
e_currentUrl="https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
a_currentUrl=browser.current_url
print("the actual current url:",a_currentUrl)
print("the expected current url:",e_currentUrl)
if e_currentUrl==a_currentUrl:
    print("gmail application opened successfully")
else:
    print("gmail applicaton failed to open")
browser.close()