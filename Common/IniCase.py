# -*- coding: utf-8 -*-

# @Time    : 2018/11/10 13:26

# @Author  : litao

# @Project : project

# @FileName: IniCase.py

# @Software: PyCharm
import yaml

from config import ConfRelevance


def ini_case(_path):
    """
    case初始化步骤
    :param _path:  case路径
    :return:
    """
    with open(_path + "/case.yaml", 'r', encoding="utf-8") as load_f:
        project_dict = yaml.load(load_f)
    rel = ConfRelevance.ConfRelevance(_path + "/relevance.ini")
    relevance = rel.get_relevance_conf()
    return project_dict, relevance
