import json
import re
from json import JSONDecodeError

from config.configHost import ConfHost

failureException = AssertionError


def manage(param, relevance):
    """
    author: 李涛
    替换关联数据
    :param param: 请求头或请求参数
    :param relevance: 关联对象
    :return:
    """
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
                            param[key] = re.sub(pattern, relevance[n], param[key])
                    except KeyError:
                        pass
            except TypeError:
                pass
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


def host_manage(host):
    try:
        relevance_list = re.findall("\${(.*?)}\$", host)  # 查找字符串中所有$key$ 作为关联对象
        for n in relevance_list:  # 遍历关联key
            pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
            host_config = ConfHost()
            host_relevance = host_config.get_host_conf()
            host = re.sub(pattern, host_relevance[n], host, count=1)
    except TypeError:
        pass
    return host


def read_param(test_name, param, relevance):
    """
    判断用例中参数类型
    :param test_name:
    :param param:
    :param relevance:
    :return:
    """
    # 用例中参数为json格式
    if isinstance(param, dict):
        param = manage(param, relevance)
    # 用例中参数非json格式
    else:
        try:
            with open(param, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    if i["test_name"] == test_name:
                        param = i["parameter"]
                        break
                if not param:
                    raise failureException("未找到用例关联的参数\n文件路径： %s\n索引： %s" % (param, test_name))
        except FileNotFoundError:
            raise failureException("用例关联文件不存在\n文件路径： %s" % param)
        except JSONDecodeError:
            raise failureException("用例关联的参数文件有误\n文件路径： %s" % param)
    return param


if __name__ == "__main__":
    # a = {"token": "test", "a": {"b": "Token $key$ $key$ $key$ $token$"}, "c": "$word$"}
    # b = {"key": ["123", "321"], "token": "test"}
    # print(manage(a, b))
    c = {"code": 0, "codeMessage": "success", "data": {"phone": "17150194892"}, "ts": 1531460245367}
    print(get_value(c, "phone"))
