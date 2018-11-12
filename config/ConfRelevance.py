# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 20:08

# @Author  : litao

# @Project : project

# @FileName: ConfRelevance.py

# @Software: PyCharm

import configparser
import logging

from Common.FunctionReplace import function_replace


class ConfRelevance:
    # 关联文件读取配置
    def __init__(self, _path):
        logging.info("初始化关联文件")
        config = configparser.ConfigParser()
        config.read(_path, encoding="utf-8")
        self.host = config["relevance"]

    def get_relevance_conf(self):
        relevance = dict()
        logging.debug("读取初始关联文件内容：   %s" % self.host.items())
        for key, value in self.host.items():
            relevance[key] = function_replace(value)
        logging.debug("初始关联内容数据处理后：   %s" % relevance)
        return relevance


if __name__ == "__main__":
    host = ConfRelevance("path")
