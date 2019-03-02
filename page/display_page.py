# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : display_page.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : 显示页面
from selenium.webdriver.common.by import By
import pytest
from base.base_action import BaseAction


class DisPlayPage(BaseAction):
    display_btn = By.XPATH, "//*[@text='显示']"  # 显示按钮
    sourch_btn = By.XPATH, "//*[@content-desc='搜索']"  # 搜索按钮
    text = By.CLASS_NAME, "android.widget.EditText"  # 文本输入框

    def display(self):
        # 点击显示
        self.click(self.display_btn)

    def sourch(self):
        # 点击搜索
        self.click(self.sourch_btn)

    def input_box(self, text):
        # 输入文本内容
        self.input_text(self.text, text)


if __name__ == '__main__':
    pytest.main("-s display_page.py")
