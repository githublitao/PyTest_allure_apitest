# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm

import json
from json import JSONDecodeError

from Common.ParamManage import manage
from main import failureException


def read_json(test_name, code_json, relevance, _path, result):
    """
    校验内容读取
    :param test_name: 用例名称，用作索引
    :param code_json: 文件路径
    :param relevance: 关联对象
    :param _path: case路径
    :param result: 全局结果
    :return:
    """
    # 用例中参数为json格式
    if isinstance(code_json, dict):
        code_json = manage(code_json, relevance)
    # 用例中参数非json格式
    else:
        try:
            with open(_path+"/"+code_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    # 遍历，通过用例名称做索引查找到第一个期望结果后，跳出循环
                    if i["test_name"] == test_name:
                        code_json = i["json"]
                        break
                # 如果code_json为空，表示未找到用例关联的期望结果
                if not code_json:
                    result["result"] = False
                    raise failureException("未找到用例关联的期望结果\n文件路径： %s\n索引： %s" % (code_json, test_name))
                else:
                    code_json = manage(code_json, relevance)
        # 文件不存在
        except FileNotFoundError:
            result["result"] = False
            raise failureException("用例关联文件不存在\n文件路径： %s" % code_json)
        # 文件存在，但里面存储的数据有误，json.load执行异常
        except JSONDecodeError:
            result["result"] = False
            raise failureException("用例关联的期望文件有误\n文件路径： %s" % code_json)
    # 返回获取的期望结果
    return code_json


if __name__ == "__main__":
    path = 'D:\\project\\PyTest_allure_apitest\\test_case\\test_01_login'
    _code_json = 'expected.json'
    _relevance = {'name': '123', 'type': 'Web', 'version': '1.2.0', 'description': '这是一个描述', 'first_name': 'Tom'}
    _result = {'result': True}
    _test_name = '登陆2'
    read_json(_test_name, _code_json, _relevance, path, _result)
