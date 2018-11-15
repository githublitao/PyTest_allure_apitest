# -*- coding: utf-8 -*-

# @Time    : 2018/11/11 9:33

# @Author  : litao

# @Project : project

# @FileName: IniRelevance.py

# @Software: PyCharm

from config import ConfRelevance


def ini_relevance(_path):
    """
    读取初始化关联文件
    :param _path:  case路径
    :return:
    """
    rel = ConfRelevance.ConfRelevance(_path + "/relevance.ini")
    relevance = rel.get_relevance_conf()
    return relevance


if __name__ == "__main__":
    print(ini_relevance('D:\\project\\PyTest_allure_apitest\\test_case\\test_01_login'))
