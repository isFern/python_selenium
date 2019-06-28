# -*- coding: UTF-8 -*-
from selenium import webdriver
import time


driver = webdriver.Chrome(r"D:\IntelliJ IDEA 15.0\workspace\yinghua\reqtest\driver\chromedriver.exe")
driver.get("https://www.baidu.com/")
print(driver.title)
driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
time.sleep(3)

'''driver.back() //回到上一个页面
driver.forward() //切换到下一个页面
driver.refresh() //重新加载页面
driver.close() //关闭当前页面
关闭所有由当前测试脚本打开的页面'''
settings = driver.find_element_by_link_text('设置')
webdriver.ActionChains(driver).move_to_element(settings).perform()

time.sleep(1)

settings_search = driver.find_element_by_class_name('setpref')
settings_search.click()

time.sleep(3)
driver.quit()
