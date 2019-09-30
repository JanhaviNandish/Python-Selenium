class Login():
    def __init__(self,chrome):
        self.chrome=chrome
        self.email_textbox="email"
        self.pwd_textbox="pass"
        self.login_link="send2"

    def type_email_text_box(self,email):
        self.chrome.find_element_by_id(id_=self.email_textbox).send_keys(email)

    def type_pwd_text_box(self, pwd):
        self.chrome.find_element_by_id(id_=self.pwd_textbox).send_keys(pwd)

    def click_login_link(self):
        self.chrome.find_element_by_id(id_=self.login_link).click()