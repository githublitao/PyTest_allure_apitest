import re


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
            relevance_list = re.findall("\$(.*?)\$", value)   # 查找字符串中所有$key$ 作为关联对象
            relevance_index = 0  # 初始化列表索引
            for n in relevance_list:  # 遍历关联key
                pattern = re.compile('\$' + n + '\$')  # 初始化正则匹配
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
    return param


def get_value(data, value):
    """
    author 李涛
    获取json中的值
    :param data: json数据
    :param value: 值
    :return:
    """
    relevance = ""
    if isinstance(data, dict):
        if value in data:
            relevance = data[value]
        else:
            for key in data:
                relevance = get_value(data[key], value)
    if isinstance(data, list):
        for key in data:
            if isinstance(key, dict):
                relevance = get_value(key, value)
                break
    return relevance


if __name__ == "__main__":
    a = {"token": "test", "a": {"b": "Token $key$ $key$ $key$ $token$"}, "c": "$word$"}
    b = {"key": ["123", "321"], "token": "test"}
    print(manage(a, b))
