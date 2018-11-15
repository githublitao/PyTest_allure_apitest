# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:09

# @Author  : litao

# @Project : project

# @FileName: ReadParam.py

# @Software: PyCharm


import json
from json import JSONDecodeError

from Common.ParamManage import manage
from main import failureException


def read_param(test_name, param, relevance, _path, result):
    """
    判断用例中参数类型
    :param test_name: 用例名称
    :param param:
    :param relevance: 关联对象
    :param _path: case路径
    :param result: 全局结果
    :return:
    """
    # 用例中参数为json格式
    if isinstance(param, dict):
        param = manage(param, relevance)
    # 用例中参数非json格式
    else:
        try:
            with open(_path+"/"+param, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    # 通过test_name索引，提取第一个匹配到的用例参数
                    if i["test_name"] == test_name:
                        param = i["parameter"]
                        break
                # 为空，未匹配到
                if not isinstance(param, dict):
                    result["result"] = False
                    raise failureException("未找到用例关联的参数\n文件路径： %s\n索引： %s" % (param, test_name))
                else:
                    param = manage(param, relevance)
        except FileNotFoundError:
            result["result"] = False
            raise failureException("用例关联文件不存在\n文件路径： %s" % param)
        except JSONDecodeError:
            result["result"] = False
            raise failureException("用例关联的参数文件有误\n文件路径： %s" % param)
    return param


if __name__ == "__main__":
    path = 'D:\\project\\PyTest_allure_apitest\\test_case\\test_02_addProject'
    _param = {}
    _relevance = {'name': '6', 'type': 'Web', 'version': 'gmRu40IPsY', 'description': 'he6xNHtSIO'}
    _result = {'result': True}
    _test_name = '登陆1'
    print(read_param(_test_name, _param, _relevance, path, _result))
