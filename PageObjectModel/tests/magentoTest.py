import time
import unittest

from selenium import webdriver

from pages.HomePage import HomePage
from pages.loginPage import Login
from pages.logoutPage import Logout


class MagentoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chrome = webdriver.Chrome(executable_path="F:\SeleniumComponents\chromedriver.exe")
        cls.chrome.maximize_window()
        cls.chrome.implicitly_wait(time_to_wait=20)
        cls.chrome.get(url="http://www.magento.com")

    @classmethod
    def tearDownClass(cls):
        cls.chrome.close()
        print("Test completed")

    def test_login_validation(self):
        home_page = HomePage(self.chrome)
        home_page.myacc_click()
        login_page = Login(self.chrome)
        login_page.type_email_text_box(email="nitinmanjunath1991@gmail.com")
        login_page.type_pwd_text_box(pwd="Welcome123")
        login_page.click_login_link()
        logout_page=Logout(self.chrome)
        logout_page.click_log_out()
        time.sleep(3)



