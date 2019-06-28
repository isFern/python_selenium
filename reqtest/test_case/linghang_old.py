# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import unittest


class LinghangTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"D:\IntelliJ IDEA 15.0\workspace\yinghua\reqtest\driver\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://ipilot.lhcoffeetime.com"
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.username = 'xxx'
        cls.password = 'xxx'

    @classmethod
    def tearDownClass(cls):
        cls.driver.refresh()
        # cls.assertEqual([], cls.verificationErrors)
        cls.driver.quit()

    def test_1Login(self):

        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(self.username)

        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.password)

        # driver.find_element_by_id("checkCode").clear()
        # driver.find_element_by_id("checkCode").send_keys("123456")

        driver.find_element_by_id('login_submit').click()
        time.sleep(5)
        print(self.driver.title)
        self.assertEqual("领航智造 —— 首页", self.driver.title, msg=None)

    def test_Customer(self):

        # 首先定位到客户中心（弹出下拉列表）
        self.driver.find_element_by_id('leftTreeNav_99_a').click()
        print(self.driver.title)
        self.assertEqual("领航智造 —— 首页", self.driver.title, msg=None)
        time.sleep(3)
        # 在客户中心下找到客户管理等菜单
        customer_menus = self.driver.find_elements_by_xpath('//*[@id="leftTreeNav_100_a"]')
        for customer_menu in customer_menus:
            customer_menu.click()
            time.sleep(3)


if __name__ == "__main__":
    unittest.main()
