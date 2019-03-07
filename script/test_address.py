# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test_address.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : null
import time
import pytest
from base.base_driver import init_driver
from base.read_file import ReadYaml
from page.address_book.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver(appPackage='com.android.contacts'
                                  , appActivity='.activities.PeopleActivity')
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"), ReadYaml(r"E:\PyWork\po\data\address_data.yaml", "test_add_contact")
                             .data_list())
    def test_address(self, name, phone):
        self.page.address().newContact()
        self.page.newAddress().addIfo(name, phone)
        self.page.newAddress().more()
        self.page.newAddress().giveUp()
        self.page.newAddress().sure()


if __name__ == '__main__':
    pytest.main('-s test_address.py')
