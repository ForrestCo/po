# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : yaml数据驱动.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : 解析 yaml 文件方法方法封装
import yaml
import os


class ReadYaml:
    def __init__(self, file_name):
        self.file_path = os.getcwd() + os.sep + 'data' + os.sep + file_name

    def return_data(self):
        with open(self.file_path, 'r') as fp:
            data = yaml.load(fp)
            return data


if __name__ == '__main__':
    read_file = ReadYaml('config.yaml')
    print(read_file.return_data())

