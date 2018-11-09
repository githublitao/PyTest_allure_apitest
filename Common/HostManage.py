# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:08

# @Author  : litao

# @Project : project

# @FileName: HostManage.py

# @Software: PyCharm


import re

from config.configHost import ConfHost


def host_manage(host):
    """
    host关联配置
    :param host:
    :return:
    """
    try:
        relevance_list = re.findall("\${(.*?)}\$", host)  # 查找字符串中所有$key$ 作为关联对象
        for n in relevance_list:  # 遍历关联key
            pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
            # 初始化host配置
            host_config = ConfHost()
            host_relevance = host_config.get_host_conf()  # 获取配置里面所有host
            host = re.sub(pattern, host_relevance[n], host, count=1)  # 替换host 1次
    except TypeError:
        pass
    return host
