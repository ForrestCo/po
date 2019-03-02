# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : tools.py
# @Author: 杨崇
# @Date  : 2019/2/28
# @Desc  : 前置代码提取封装
from appium import webdriver


def init_driver(platformName='Android', platformVersion='5',
                   deviceName='192.168.46.101:5555', appPackage='com.android.settings',
                   appActivity='.Settings'):
    desired_caps = dict()
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


if __name__ == '__main__':
    init_driver()
