# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : page.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : null
from page.address_book.address_page import AddressPage
from page.address_book.new_address_page import NewAddress
from page.address_book.popups_page import PopupsPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def address(self):
        return AddressPage(self.driver)

    def newAddress(self):
        return NewAddress(self.driver)

    def popups(self):
        return PopupsPage(self.driver)
