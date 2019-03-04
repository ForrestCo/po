# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : setting_page.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : 设置页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SetPage(BaseAction):
    more_btn = By.XPATH, "//*[@text='更多']"  # 更多
    display_btn = By.XPATH, "//*[@text='显示']"  # 显示

    # ********************************

    # big = By.XPATH, "//*[@text='无线网络']"

    def more(self):
        self.click(self.more_btn)

    def display(self):
        self.click(self.display_btn)

    # # 进入无线网络
    # def bigBan(self):
    #     self.click(self.big)
