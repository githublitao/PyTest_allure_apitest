# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm


import re

import jsonpath

from Common.FunctionReplace import function_replace
from Exception.CustomException import RelevanceIndexError, RelevanceIndexNotInt, RelevanceValueError


def manage(param, relevance):
    """
    替换关联数据
    :param param: 请求头或请求参数或期望
    :param relevance: 关联对象
    :return:
    """
    if isinstance(param, dict):  # 判断类型元字典，递归
        for key, value in param.items():  # 遍历参数
            if isinstance(value, dict):  # 判断类型元字典，递归
                param[key] = manage(value, relevance)
            elif isinstance(value, list):  # 判断列表类型，遍历递归
                for k, i in enumerate(value):
                    param[key][k] = manage(i, relevance)
            else:  # 字符串类型
                try:
                    relevance_list = re.findall("\${(.*?)}\$", value)   # 查找字符串中所有$key$ 作为关联对象
                    for n in relevance_list:  # 遍历关联key
                        pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
                        n_list = n.split(".")
                        n = n.lower()
                        try:
                            if len(n_list) == 1:
                                param[key] = re.sub(pattern, str(relevance[n]), param[key])
                            elif len(n_list) == 2:
                                if n_list[1].isdigit():
                                    try:
                                        param[key] = re.sub(pattern, str(relevance[n_list[0]][int(n_list[1])]), param[key])
                                    except IndexError:
                                        raise RelevanceIndexError(relevance[n], n)
                                else:
                                    raise RelevanceIndexNotInt(n)
                            else:
                                raise RelevanceValueError(n)
                        except KeyError:
                            pass
                except TypeError:
                    pass
                try:
                    param[key] = function_replace(param[key])
                except TypeError:
                    pass

    elif isinstance(param, list):
        for k, i in enumerate(param):
            param[k] = manage(i, relevance)
    else:  # 字符串类型
        try:
            relevance_list = re.findall("\${(.*?)}\$", param)  # 查找字符串中所有$key$ 作为关联对象
            for n in relevance_list:  # 遍历关联key
                pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
                n_list = n.split(".")
                n = n.lower()
                if len(n_list) == 1:
                    param = re.sub(pattern, str(relevance[n]), param)
                elif len(n_list) == 2:
                    if isinstance(n_list[1], int):
                        try:
                            param = re.sub(pattern, str(relevance[n_list[0]][int(n_list[1])]), param)
                        except IndexError:
                            raise RelevanceIndexError(relevance[n], n)
                    else:
                        raise RelevanceIndexNotInt(n)
                else:
                    raise RelevanceValueError(n)
        except TypeError:
            pass
        try:
            param = function_replace(param)
        except TypeError:
            pass
    return param


if __name__ == "__main__":
    pass
    # a = {"token": "test", "a": {"b": "Token $key$ $key$ $key$ $token$"}, "c": "$word$"}
    # b = {"key": ["123", "321"], "token": "test"}
    # print(manage(a, b))
    # c = {'name': '10', 'type': 'Web', 'version': 'KHQdpM8gAL', 'description': 'avp7tZOyiY', 'key': ['e1dfbfd759ad46bcdc44df989ade3f1c190cc936', '313vda']}
    # # b = get_value(c, "$.key[1]")
    # if b:
    #     print(type(b))
    #     print(b)
