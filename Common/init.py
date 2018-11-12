# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import logging
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
        logging.info("执行测试用例前置接口")
        with allure.step("接口关联请求"):
            for i in case_dict["premise"]:
                relevance_list = relevance.copy()
                for j in range(0, 3):
                    # 获取前置接口关联数据失败
                    code, data = send_request(i, case_dict["testinfo"].get("host"),
                                              case_dict["testinfo"].get("address"), relevance_list, _path)
                    if not data:
                        with allure.step("接口请求失败！等待三秒后重试！"):
                            pass
                        logging.info("接口请求失败！等待三秒后重试！")
                        continue
                    if i["relevance"]:
                        if len(i["relevance"]):
                            relevance = get_relevance(data, i["relevance"], relevance)
                            if isinstance(relevance, bool):
                                with allure.step("从结果中提取关联键的值失败！等待3秒后重试！"):
                                    pass
                                logging.info("从结果中提取关联键的值失败！等待3秒后重试！")
                                time.sleep(3)
                                continue
                            else:
                                break
                        else:
                            break
                    else:
                        break
                if isinstance(relevance, bool):
                    logging.info("从结果中提取关联键的值失败！重试三次失败")
                    raise failureException("获取前置接口关联数据失败")
    return relevance

