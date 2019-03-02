# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : mobile_page.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : 移动网络页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MobileNetWorkPage(BaseAction):
    first_network_type_btn = By.XPATH, "//*[@text='首选网络类型']"

    def first_network_type(self):
        self.click(self.first_network_type_btn)
