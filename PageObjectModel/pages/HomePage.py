class HomePage():
    def __init__(self,chrome):
        self.chrome=chrome
        self.myacc_link = "My Account"

    def myacc_click(self):
        self.chrome.find_element_by_link_text(link_text=self.myacc_link).click()