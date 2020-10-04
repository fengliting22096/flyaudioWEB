

class BasePages:
    def __init__(self, driver):
        self.driver = driver

    def input(self,element,test):
        try:
            self.driver.find_element(*element).send_keys(test)
        except:
            print("没找到元素:" + str(element))
            raise
    def el_click(self,element):
        try:
            self.driver.find_element(*element).click()
        except:
            print("没找到元素:" + str(element))
            raise

    def get_text(self,element):
        try:
            return self.driver.find_element(*element).text
        except:
            print("没找到元素:" + str(element))
            raise
    def url(self, addr):
        try:
            self.driver.get(addr)
        except:
            print("地址错误:"+addr)
            raise
    def headle(self,element):
        try:
            self.driver.find_element(*element)
        except:
            print("没找到元素:" + str(element))
            raise

    def display(self, element):
        try:
            return self.driver.find_element(*element).is_displayed()
        except:
            print("没找到元素:" + str(element))
            raise