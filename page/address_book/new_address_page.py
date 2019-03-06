# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : new_address_page.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : 新建联系人页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewAddress(BaseAction):
    # 姓名
    add_name = By.XPATH, "//*[@text='姓名']"
    # 电话
    add_phone = By.XPATH, "//*[@text='电话']"
    # 更多按钮
    more_btn = By.CLASS_NAME, "android.widget.ImageButton"
    # 舍弃更改
    giveup_btn = By.XPATH, "//*[@text='舍弃更改']"

    sure_btn = By.XPATH, "//*[@text='确定']"

    def addIfo(self, name, phone):
        self.input_text(self.add_name, name)
        self.input_text(self.add_phone, phone)

    def more(self):
        self.find_elements(self.more_btn)[1].click()

    def giveUp(self):
        self.click(self.giveup_btn)

    def sure(self):
        self.click(self.sure_btn)
