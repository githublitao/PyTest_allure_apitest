# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import configparser
import os

PATH = os.path.split(os.path.realpath(__file__))[0]


class ConfHost:
    # host文件读取配置
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(PATH+"/host.ini", encoding="utf-8")
        self.host = config["host"]

    def get_host_conf(self):
        return self.host


if __name__ == "__main__":
    host = ConfHost()
    for k, v in host.get_host_conf():
        print(k, v)

