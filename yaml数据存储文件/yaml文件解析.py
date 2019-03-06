# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : yaml文件解析.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : null
import yaml

# 读取 yaml 文件
# with open('./data/config.yaml', 'r') as fp:
#     data = yaml.load(fp)
#     print(data)
#     print(type(data))

# 写入yaml文件

# 文件内容
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 写入yaml文件
with open('./data/demo.yaml', 'w') as fp:
    yaml.dump(data, fp)
