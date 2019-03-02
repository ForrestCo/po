# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : first_network_type.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : 首选网络类型页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstNetWorkType(BaseAction):
    type_3G_btn = By.XPATH, "//*[@text='3G']"
    type_2G_btn = By.XPATH, "//*[@text='2G']"

    def type_3G(self):
        self.click(self.type_3G_btn)

    def type_2G(self):
        self.click(self.type_2G_btn)

