# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import logging

from Common.ParamManage import get_value


def get_relevance(data, relevance_list, relevance):
    """
    从返回结果中获取关联键的值
    :param data:  返回结果
    :param relevance_list:  关联键列表
    :param relevance: 关联对象
    :return:
    """
    # 关联键是否时list
    if not relevance_list:
        return relevance
    logging.debug("从返回结果中根据关联键%s提取值" % relevance_list)
    if isinstance(relevance_list, list):
        # 遍历关联键
        for j in relevance_list:
            # 从结果中提取关联键的值
            relevance_value = get_value(data, j)
            if relevance_value:
                # 考虑到一个关联键，多个值
                if j in relevance:
                    if isinstance(relevance[j], list):
                        a = relevance[j]
                        a.append(relevance_value)
                        relevance[j] = a
                    else:
                        a = relevance[j]
                        b = list()
                        b.append(a)
                        b.append(relevance_value)
                        relevance[j] = b
                else:
                    relevance[j] = relevance_value
            else:
                return False
    else:
        relevance_value = get_value(data, relevance_list)
        if relevance_value:
            # 考虑到一个关联键，多个值
            if relevance_list in relevance:
                if isinstance(relevance_list, list):
                    a = relevance[relevance_list]
                    a.append(relevance_value)
                    relevance[relevance_list] = a
                else:
                    a = relevance[relevance_list]
                    b = list()
                    b.append(a)
                    b.append(relevance_value)
                    relevance[relevance_list] = a
            else:
                relevance[relevance_list] = relevance_value
    logging.debug("提取后，关联键对象\n%s" % relevance)
    return relevance


if __name__ == "__main__":
    _data = {'code': '999999', 'msg': '成功', 'data': {'first_name': 'Tom', 'last_name': '', 'phone': '123456789', 'email': '123@qq.com', 'key': 'e1dfbfd759ad46bcdc44df989ade3f1c190cc936', 'date_joined': '2018-06-28 02:54:00', 'userphoto': '/file/userphoto.jpg'}}
    _relevance = {'name': '10', 'type': 'Web', 'version': 'KHQdpM8gAL', 'description': 'avp7tZOyiY'}
    _relevance_list = ['key']
    print(get_relevance(_data, _relevance, _relevance_list))

