# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : page.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : xxx_page统一入口
from page.display_page import DisPlayPage
from page.first_network_type import FirstNetWorkType
from page.mobile_network_page import MobileNetWorkPage
from page.more_page import MorePage
from page.setting_page import SetPage


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    # 设置页面
    def setting(self):
        return SetPage(self.driver)

    # 更多
    def more(self):
        return MorePage(self.driver)

    # 移动网络
    def mobile_network(self):
        return MobileNetWorkPage(self.driver)

    # 首选网络类型
    def first_network_type(self):
        return FirstNetWorkType(self.driver)

    # 显示
    def display(self):
        return DisPlayPage(self.driver)
