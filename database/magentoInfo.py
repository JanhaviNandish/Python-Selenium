import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver.exe")
        cls.chrome.maximize_window()
        cls.chrome.implicitly_wait(time_to_wait=20)
        cls.chrome.get(url="http://www.magento.com")

    def test_login_Operator(self):
        self.chrome.find_element_by_xpath("//a[text()='My Account']").click()
        self.chrome.find_element_by_xpath("//input[@id='email']").send_keys("nitinmanjunath1991@gmail.com")
        self.chrome.find_element_by_xpath("//input[@id='pass']").send_keys("Welcome123")
        self.chrome.find_element_by_xpath("//button[@id='send2']").click()
        self.chrome.find_element_by_xpath("//a[text()='Log Out']").click()
    @classmethod
    def tearDownClass(cls):
        cls.chrome.close()
        print("Test completed")