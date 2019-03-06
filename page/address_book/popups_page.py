# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : popups_page.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : 弹窗
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PopupsPage(BaseAction):
    # 本地保存
    local_save_btn = By.XPATH, "//*[@text='本地保存']"
    # 添加账户
    add_account_btn = By.XPATH, "//*[@text='添加账户']"

    def localSave(self):
        self.click(self.local_save_btn)

    def addAcount(self):
        self.click(self.add_account_btn)
