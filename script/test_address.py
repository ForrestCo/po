# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test_address.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : null
import time

from base.base_driver import init_driver
from page.address_book.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver(appPackage='com.android.contacts', appActivity='.activities.PeopleActivity')
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_address(self):
        self.page.address().newContact()
        self.page.popups().localSave()
        self.page.newAddress().addIfo('name', '110')
        time.sleep(2)
        self.page.newAddress().more()
        time.sleep(2)
        self.page.newAddress().giveUp()
        self.page.newAddress().sure()
