# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : more_page.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : 更多页面
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MorePage(BaseAction):
    # more_btn = By.XPATH, "//*[@text='更多']"
    network_btn = By.XPATH, "//*[@text='移动网络']"  # 移动网络
    # type_btn = By.XPATH, "//*[@text='首选网络类型']"
    # select2G_btn = By.XPATH, "//*[@text='2G']"
    # select3G_btn = By.XPATH, "//*[@text='3G']"

    # def more(self):
    #     self.click(self.more_btn)

    def network(self):
        self.click(self.network_btn)

    # def type(self):
    #     self.click(self.type_btn)
    #
    # def select2G(self):
    #     self.click(self.select2G_btn)
    #
    # def select3G(self):
    #     self.click(self.select3G_btn)
