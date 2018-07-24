#encoding=utf8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#父类是unittest.TestCase
class PythonOrgSearch(unittest.TestCase):
    #测试前准备环境的搭建
    def setUp(self):
        self.driver = webdriver.Ie()
    #定义测试用例要以test_开头
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        print(self.assertIn("Python", driver.title))
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
     #测试后环境的还原(tearDown)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    #自动执行以“test”命名开头的测试方法
    unittest.main()