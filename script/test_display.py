# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test_display.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : null
import time
from base.base_driver import init_driver
from appium import webdriver
import pytest

from page.display_page import DisPlayPage


class TestDisplay(object):
    def setup(self):
        # 设置参数
        self.driver = init_driver()
        self.page = DisPlayPage(self.driver)
        print("--------setup执行------------")

    def test_display(self):

        self.page.test_more()

    def teardown(self):
        time.sleep(2)
        print("--------teardown------------")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main("-s test_setting.py")
