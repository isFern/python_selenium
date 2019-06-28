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

        resp = requests.get(self.base_url, timeout=5)
        self.code = resp.status_code
        print(self.driver.title)
        print(self.code)
        self.assertEqual(200, self.code, msg=None)

    def test_Customer(self):

        '''base_url = 'http://ipilot.lhcoffeetime.com/bugu-web-front/web/capital/device/'
        menulist = ['deviceExport.html','deviceStock.html','deviceInput.html']
        '''
        level0s = self.driver.find_elements_by_css_selector("li[class='level0']")
        print("num of level0: %d" % len(level0s))
        for i in range(0, len(level0s)):
            print("level00000: %s" % level0s[i].text)
            level0s[i].click()

            url = self.driver.current_url
            print(u"获取当前页面url :%s" % url)
            resp = requests.get(url, timeout=5)
            self.code = resp.status_code
            self.assertEqual(200, self.code, msg=None)

            level0s = self.driver.find_elements_by_css_selector("li[class='level0']")
            level1s = self.driver.find_elements_by_css_selector("li[class='level1']")
            time.sleep(3)
            print("num of level1: %d" % len(level1s))

            for j in range(0, len(level1s)):
                print("level11111: %s" % level1s[j].text)
                level1s[j].click()

                url = self.driver.current_url
                print(u"获取当前页面url :%s" % url)
                resp = requests.get(url, timeout=5)
                self.code = resp.status_code
                self.assertEqual(200, self.code, msg=None)

                level1s = self.driver.find_elements_by_css_selector("li[class='level1']")
                level2s = self.driver.find_elements_by_css_selector("li[class='level2']")
                time.sleep(3)
                if j == (len(level1s)-1):
                    level1s[i].click()
                print("num of level2: %d" % len(level2s))

                for p in range(0, len(level2s)):
                    print("level22222: %s" % level2s[p].text)
                    level2s[p].click()

                    url = self.driver.current_url
                    print(u"获取当前页面url :%s" % url)
                    resp = requests.get(url, timeout=5)
                    self.code = resp.status_code
                    self.assertEqual(200, self.code, msg=None)

                    level2s = self.driver.find_elements_by_css_selector("li[class='level2']")
                    level1s = self.driver.find_elements_by_css_selector("li[class='level1']")
                    time.sleep(3)
                    print(level1s[j])
                    if p == (len(level2s)-1):
                        level1s[j].click()


if __name__ == "__main__":
    unittest.main()
