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
        print(self.get_text(lookfor.text))
        self.el_click(lookfor.diyi)
        sleep(2)

    def get_url(self):
        self.url("https://www.w3school.com.cn/tiy/t.asp?f=js_alert")

        self.driver.switch_to.frame("iframeResult")
        self.el_click(lookfor.jc)
        self.driver.switch_to.alert.accept()
        sleep(3)



