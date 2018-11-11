# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import time

import allure

from Common.GetRelevance import get_relevance
from Common.requestSend import send_request
from main import failureException


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
                relevance_list = relevance.copy()
                for j in range(0, 3):
                    # 获取前置接口关联数据失败
                    code, data = send_request(i, case_dict["testinfo"].get("host"),
                                              case_dict["testinfo"].get("address"), relevance_list, _path)
                    if i["relevance"]:
                        if len(i["relevance"]):
                            relevance = get_relevance(data, i["relevance"], relevance)
                            if isinstance(relevance, bool):
                                time.sleep(3)
                                continue
                            else:
                                break
                        else:
                            break
                    else:
                        break
                if isinstance(relevance, bool):
                    raise failureException("获取前置接口关联数据失败")
    return relevance

