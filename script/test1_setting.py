# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test_setting.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : null
import time
from base.base_driver import init_driver
from appium import webdriver
import pytest


# - 更多-移动网络-首选网络类型-点击2G
# - 更多-移动网络-首选网络类型-点击3G
# - 显示-搜索按钮-输入hello-点击返回

class TestSeting(object):
    def setup(self):
        # 设置参数
        self.driver = init_driver()
        print("--------setup执行------------")

    def test_2G(self):
        self.driver.find_element_by_xpath("//*[@text='更多']").click()
        self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.driver.find_element_by_xpath("//*[@text='2G']").click()

    def test_3G(self):
        self.driver.find_element_by_xpath("//*[@text='更多']").click()
        self.driver.find_element_by_xpath("//*[@text='移动网络']").click()
        self.driver.find_element_by_xpath("//*[@text='首选网络类型']").click()
        self.driver.find_element_by_xpath("//*[@text='3G']").click()

    def test_display(self):
        self.driver.find_element_by_xpath("//*[@text='显示']").click()
        self.driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()

    def teardown(self):
        time.sleep(2)
        print("--------teardown------------")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main("-s test_setting.py")
