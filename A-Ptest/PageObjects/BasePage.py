

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
