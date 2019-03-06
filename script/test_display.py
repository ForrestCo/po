# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test_display.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : null
import time
from base.base_driver import init_driver
import pytest

from page.page import Page


class TestDisplay(object):
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        print("--------setup执行------------")

    def test_display(self):
        # 进入显示页面
        self.page.setting.display()
        # 搜索
        self.page.display.sourch()
        # 输入文字
        self.page.display.input_box("123456")

    def teardown(self):
        time.sleep(2)
        print("--------teardown------------")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main("-s test_setting.py")
