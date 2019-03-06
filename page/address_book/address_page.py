# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : address.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : 通讯录页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressPage(BaseAction):
    # 新建联系人
    btn_newContact = By.ID, 'com.android.contacts:id/floating_action_button'

    def newContact(self):
        self.click(self.btn_newContact)
