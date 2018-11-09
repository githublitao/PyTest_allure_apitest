# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm

import json
from json import JSONDecodeError

failureException = AssertionError


def read_json(test_name, code_json):
    """
    校验内容读取
    :param test_name: 用例名称，用作索引
    :param code_json: 文件路径
    :return:
    """
    # 用例中参数为json格式
    if isinstance(code_json, dict):
        pass
    # 用例中参数非json格式
    else:
        try:
            with open(code_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    # 遍历，通过用例名称做索引查找到第一个期望结果后，跳出循环
                    if i["test_name"] == test_name:
                        code_json = i["json"]
                        break
                # 如果code_json为空，表示未找到用例关联的期望结果
                if not code_json:
                    raise failureException("未找到用例关联的期望结果\n文件路径： %s\n索引： %s" % (code_json, test_name))
        # 文件不存在
        except FileNotFoundError:
            raise failureException("用例关联文件不存在\n文件路径： %s" % code_json)
        # 文件存在，但里面存储的数据有误，json.load执行异常
        except JSONDecodeError:
            raise failureException("用例关联的期望文件有误\n文件路径： %s" % code_json)
    # 返回获取的期望结果
    return code_json

