from PageObjects.Elements.elements import lookfor
from time import sleep
from PageObjects.BasePage import BasePages


class Home_Page_test(BasePages):
    def search(self):
        text = "击鼓"
        self.input(lookfor.search_shici, text)
        sleep(2)
        self.el_click(lookfor.icon)
        sleep(3)
        self.el_click((lookfor.black))
        sleep(2)


