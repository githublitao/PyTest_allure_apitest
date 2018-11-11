# -*- coding: utf-8 -*-

# @Time    : 2018/11/11 9:33

# @Author  : litao

# @Project : project

# @FileName: IniRelevance.py

# @Software: PyCharm
from config import ConfRelevance


def ini_relevance(_path):
    rel = ConfRelevance.ConfRelevance(_path + "/relevance.ini")
    relevance = rel.get_relevance_conf()
    return relevance
