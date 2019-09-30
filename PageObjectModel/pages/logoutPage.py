class Logout():
    def __init__(self,chrome):
        self.chrome=chrome
        self.logout_link="Log Out"

    def click_log_out(self):
        self.chrome.find_element_by_link_text(link_text=self.logout_link).click()