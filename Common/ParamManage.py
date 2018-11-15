# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm


import re

from Common.FunctionReplace import function_replace


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
                    relevance_index = 0  # 初始化列表索引
                    for n in relevance_list:  # 遍历关联key
                        pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
                        n = n.lower()
                        try:
                            if isinstance(relevance[n], list):   # 判断是关联key是否是个list
                                try:
                                    # 替换第一个匹配到的关联
                                    param[key] = re.sub(pattern, relevance[n][relevance_index], param[key], count=1)
                                    relevance_index += 1
                                except IndexError:
                                    # 关联值使用完后，初始化索引为0，重新匹配
                                    relevance_index = 0
                                    param[key] = re.sub(pattern, relevance[n][relevance_index], param[key], count=1)
                                    relevance_index += 1
                            else:
                                # 关联key是字符串，直接替换
                                param[key] = re.sub(pattern, relevance[n], param[key], count=1)
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
            relevance_index = 0  # 初始化列表索引
            for n in relevance_list:  # 遍历关联key
                pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
                try:
                    if isinstance(relevance[n], list):  # 判断是关联key是否是个list
                        try:
                            # 替换第一个匹配到的关联
                            param = re.sub(pattern, relevance[n][relevance_index], param, count=1)
                            relevance_index += 1
                        except IndexError:
                            # 关联值使用完后，初始化索引为0，重新匹配
                            relevance_index = 0
                            param = re.sub(pattern, relevance[n][relevance_index], param, count=1)
                            relevance_index += 1
                    else:
                        # 关联key是字符串，直接替换
                        param = re.sub(pattern, relevance[n], param)
                except KeyError:
                    pass
        except TypeError:
            pass
        # try:
        #     param = function_replace(param)
        # except TypeError:
        #     pass
    return param


_relevance = ""


def get_value(data, value):
    """
    author 李涛
    获取json中的值
    :param data: json数据
    :param value: 值
    :return:
    """
    global _relevance
    if isinstance(data, dict):
        if value in data:
            _relevance = data[value]
        else:
            for key in data:
                _relevance = get_value(data[key], value)
    elif isinstance(data, list):
        for key in data:
            if isinstance(key, dict):
                _relevance = get_value(key, value)
                break
    return _relevance


if __name__ == "__main__":
    # a = {"token": "test", "a": {"b": "Token $key$ $key$ $key$ $token$"}, "c": "$word$"}
    # b = {"key": ["123", "321"], "token": "test"}
    # print(manage(a, b))
    c = {"code": 0, "codeMessage": "success", "data": {"phone": "17150194892"}, "ts": 1531460245367}
    print(get_value(c, "phone"))
