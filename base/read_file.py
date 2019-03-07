# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : read_file.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : null
import yaml


class ReadYaml:
    def __init__(self, file_path, ele_name):
        self.file_path = file_path
        self.ele_name = ele_name
        self.data = self.return_data()

    def return_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as fp:
            data = yaml.load(fp)
            return data

    def data_list(self):
        temp = self.data[self.ele_name]
        res_li = []
        for i in temp.values():
            print(i.values())
            li = []
            for j in i.values():
                li.append(j)
            res_li.append(li)
        return res_li


if __name__ == '__main__':
    read_file = ReadYaml('../data/address_data.yaml', "test_add_contact")
    print(read_file.return_data())
    print(read_file.data_list())
