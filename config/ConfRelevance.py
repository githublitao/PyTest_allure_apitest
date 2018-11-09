# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 20:08

# @Author  : litao

# @Project : project

# @FileName: ConfRelevance.py

# @Software: PyCharm

import configparser


class ConfRelevance:
    # host文件读取配置
    def __init__(self, _path):
        config = configparser.ConfigParser()
        config.read(_path, encoding="utf-8")
        self.host = config["relevance"]

    def get_relevance_conf(self):
        relevance = dict()
        for key, value in self.host.items():
            relevance[key] = value
        return relevance


if __name__ == "__main__":
    host = ConfRelevance("path")
