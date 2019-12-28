from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

path = input("请输入文件保存路径")
chrom = r":\python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom)
driver.implicitly_wait(10)
driver.maximize_window()

url = ''