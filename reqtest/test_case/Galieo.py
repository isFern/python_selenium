# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import unittest


class GalieoTest(unittest.TestCase):

    driver = webdriver.Chrome(r"D:\IntelliJ IDEA 15.0\workspace\yinghua\reqtest\driver\chromedriver.exe")
    driver.get("http://galileo-test.yunext.com")
    driver.maximize_window()
    username = 'xxx'
    password = 'xxx'

    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(username)

    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_id("checkCode").clear()
    driver.find_element_by_id("checkCode").send_keys("123456")

    driver.find_element_by_css_selector('button').click()
    time.sleep(5)

    def test_Login(self):

        print(self.driver.title)
        self.assertEqual("服务器管理 - 海大物联", self.driver.title, msg=None)
        # assert u"海大物联" in self.driver.title

    def test_Customer(self):

        # 首先定位到客户中心（弹出下拉列表）
        self.driver.find_element_by_xpath('//*[@id="root"]/div/section/aside/div/ul/li[4]/div').click()
        time.sleep(3)
        # 在客户中心下找到客户管理等菜单
        customer_menus = self.driver.find_elements_by_xpath('//*[@id="/customer$Menu"]/li')
        for customer_menu in customer_menus:
            customer_menu.click()
            time.sleep(3)
    # driver.quit()

if __name__ == "__main__":
    unittest.main()
    GalieoTest.driver.close()
    GalieoTest.driver.quit()







