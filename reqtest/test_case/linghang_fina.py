# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import unittest
import requests


class LinghangTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"D:\IntelliJ IDEA 15.0\workspace\yinghua\reqtest\driver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://ipilot.lhcoffeetime.com"
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.username = 'xxx'
        cls.password = 'xxx'

    @classmethod
    def tearDownClass(cls):

        # cls.driver.refresh()
        # cls.assertEqual([], cls.verificationErrors)
        cls.driver.quit()

    def test_1Login(self):

        driver = self.driver

        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(self.username)

        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.password)

        # driver.find_element_by_id("checkCode").clear()
        # driver.find_element_by_id("checkCode").send_keys("123456")

        driver.find_element_by_id('login_submit').click()
        time.sleep(5)

        driver.get(self.base_url)
        resp = requests.get(self.base_url, timeout=5)
        self.code = resp.status_code
        print(self.driver.title)
        print(self.code)
        self.assertEqual(200, self.code, msg=None)

    def test_Customer(self):

        level0s = self.driver.find_elements_by_xpath('//*[@id="leftTreeNav"]/li')
        print("num of level0: %d" % len(level0s))
        for i in range(1, len(level0s)):
            level0s = self.driver.find_elements_by_xpath('//*[@id="leftTreeNav"]/li')
            print("level00000: %s" % level0s[i].text)
            level0s[i].click()

            url = self.driver.current_url
            print(u"获取当前页面url :%s" % url)
            resp = requests.get(url, timeout=5)
            self.code = resp.status_code
            self.assertEqual(200, self.code, msg=None)

            print("第一层----------------------------------------------------------------------------")
            level0s = self.driver.find_elements_by_xpath('//*[@id="leftTreeNav"]/li')
            level0id = level0s[i].get_attribute('id')
            print("level0id: %s" % level0id)
            level1s = self.driver.find_elements_by_xpath("//*[@id = '" + level0id + "']/ul/li")
            time.sleep(3)
            print("num of level0: %d" % len(level0s))
            print("num of level1: %d" % len(level1s))
            for j in range(0, len(level1s)):
                level1s = self.driver.find_elements_by_xpath("//*[@id = '" + level0id + "']/ul/li")
                print("level11111: %s" % level1s[j].text)
                level1s[j].click()

                url = self.driver.current_url
                print(u"获取当前页面url :%s" % url)
                resp = requests.get(url, timeout=5)
                self.code = resp.status_code
                self.assertEqual(200, self.code, msg=None)

                level1s = self.driver.find_elements_by_xpath("//*[@id = '" + level0id + "']/ul/li")
                level1id = level1s[j].get_attribute('id')
                print("level1id: %s" % level1id)
                level2s = self.driver.find_elements_by_xpath("//*[@id = '" + level1id + "']/ul/li")
                time.sleep(3)
                print("num of level2: %d" % len(level2s))

                for p in range(0, len(level2s)):
                    level2s = self.driver.find_elements_by_xpath("//*[@id = '" + level1id + "']/ul/li")
                    print("level22222: %s" % level2s[p].text)
                    level2s[p].click()
                    time.sleep(3)

                    url = self.driver.current_url
                    print(u"获取当前页面url :%s" % url)
                    resp = requests.get(url, timeout=5)
                    self.code = resp.status_code
                    self.assertEqual(200, self.code, msg=None)

if __name__ == "__main__":
    unittest.main()

'''注意事项：
            1.每次点击后页面会刷新，在下次使用相同的元素时需要重新定位
            2.选择定位元素的方式也很重要
            '''
