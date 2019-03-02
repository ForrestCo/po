# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : base_action.py
# @Author: 杨崇
# @Date  : 2019/3/1
# @Desc  : null
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver

    # 定位一个元素
    def find_element(self, location, timeout=10, poll=1):
        # location_by(定位方式)  location_value（定位元素的属性值）
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        # 返回一个元素对象
        return wait.until(lambda x: x.driver.find_element(location_by, location_value))

    # 定位一组元素对象
    def find_elements(self, location, timeout=10, poll=1):
        location_by, location_value = location
        waite = WebDriverWait(self.driver, timeout, poll)
        return waite.until(lambda x: x.driver.find_element(location_by, location_value))

    # 点击事件
    def click(self, location):
        location_by, location_value = location
        self.driver.find_element(location_by, location_value).click()

    # 文本框输入
    def input_text(self, location, text):
        location_by, location_value = location
        self.driver.find_element(location_by, location_value).send_keys(text)
