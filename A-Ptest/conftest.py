import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PageObjects.Page_test.Home_Page import Home_Page_test

@pytest.fixture(scope='class', autouse=True)
def Start():
    path = "d:/chromedriver.exe"
    """定义全局浏览器驱动"""
    global driver
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    print("开始")
    driver.get("https://www.shicimingju.com")
    intext = Home_Page_test(driver)
    yield (driver, intext)
    print("结束")
    # 清除浏览器缓存
    driver.get("chrome://settings/clearBrowserData")
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    driver.quit()

# @pytest.fixture(scope="function", autouse=True)
# def

