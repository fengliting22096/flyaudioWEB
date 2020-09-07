
[运行结构]
POM:---将页面基本操作（点击、输入、滑动...）、元素定位分开，这样根据测试用例集成在有个Testcaes中，后续只需要维护好元素element.py表了
     从底层到测试用例
    (1)封装元素：PageObjects/Elements/elements.py
        收取页面元素，并对象化，后面UI有改动时可以在里面重新赋值
    (2)封装函数：PageObjects/BasePage.py
        封装基本操作、常用函数
    (3)页面操作：PageObjects/Page_test/Home_Page
        继承（2）封装函数，从（1）里面收取元素来进行页面操作，如点击输入控件，输入文字，获取文件
        等基本页面操作
    (4)：conftest.py
        配置启动浏览器fixture函数，使用yield传送driver驱动和页面操作模块（PageObjects/Page_test/Home_Page）
        等待执行完后返回到conftest运行后续
    (5）测试用例：testcases/*test.py
        受到conftest的控制来运行测试用例

conftest.py:
            配置fixture

pytest.ini:
           配置pytest运行参数

常见异常：
        （1）打不开浏览器：
             浏览器打不开先排查一下浏览器driver驱动路径下有没有，第二驱动版本要跟对应要启动的浏览器一致或者相差不大