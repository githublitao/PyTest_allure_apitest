# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm

import allure

from Common.GetRelevance import get_relevance
from Common.requestSend import send_request


def ini_request(case_dict, relevance, _path):
    """
    用例前提条件执行，提取关联键
    :param case_dict: 用例对象
    :param relevance:  关联对象
    :param _path:  case路径
    :return:
    """
    if isinstance(case_dict["premise"], list):
        with allure.step("接口关联请求"):
            for i in case_dict["premise"]:
                code, data = send_request(i, case_dict["testinfo"].get("host"),
                                          case_dict["testinfo"].get("address"), relevance, _path)
                # 提取关联键值
                relevance = get_relevance(data, i["relevance"], relevance)
    return relevance

