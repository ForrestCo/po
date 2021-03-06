# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test_more.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : 把测试脚本按功能进行拆分，按照页面的形式，拆分成多个
import time

import pytest

from base.base_driver import init_driver
from page.page import Page


class TestMore(object):
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        print("--------setup执行------------")

    def test_2G(self):
        self.page.setting.more()  # 进入设置页面点击更多
        self.page.more.network()  # 进入更多页面点击移动网络
        self.page.mobile_network.first_network_type()  # 进入移动网络页面点击首选网络
        self.page.first_network_type.type_2G()  # 进入首选网络点击 2G 网络

    def test_3G(self):
        self.page.setting.more()
        self.page.more.network()
        self.page.mobile_network.first_network_type()
        self.page.first_network_type.type_3G()

    def teardown(self):
        time.sleep(3)
        print("--------teardown------------")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main('-s test_more.py')

