# -*- coding: utf-8 -*-

# @Time    : 2018/11/11 17:07

# @Author  : litao

# @Project : project

# @FileName: FunctionReplace.py

# @Software: PyCharm
import re

from RandomData import RandomString, RandomInt, RandomFloat, GetTime


def function_replace(value):
    """
    调用定义方法替换字符串
    :param value:
    :return:
    """
    string_list = re.findall("\$RandomString\((.*?)\)\$", value)
    for n in string_list:
        pattern = re.compile('\$RandomString\(' + n + '\)\$')  # 初始化正则匹配
        k = RandomString.random_string(n)
        value = re.sub(pattern, k, value, count=1)
    int_list = re.findall("\$RandomInt\((.*?)\)\$", value)
    for n in int_list:
        if len(n.split(",")) == 2:
            pattern = re.compile('\$RandomInt\(' + n + '\)\$')  # 初始化正则匹配
            k = str(RandomInt.random_int(n))
            value = re.sub(pattern, k, value, count=1)
    float_list = re.findall("\$RandomFloat\((.*?)\)\$", value)
    for n in float_list:
        if len(n.split(",")) == 3:
            pattern = re.compile('\$RandomFloat\(' + n + '\)\$')  # 初始化正则匹配
            k = str(RandomFloat.random_float(n))
            value = re.sub(pattern, k, value, count=1)
    time_list = re.findall("\$GetTime\((.*?)\)\$", value)
    for n in time_list:
        time_type = re.findall("time_type=(.*?),", n)
        layout = re.findall("layout=(.*?),", n)
        unit = re.findall("unit=(.*?)", n)
        if len(time_type) and len(layout):
            pattern = re.compile('\$GetTime\(' + n + '\)\$')  # 初始化正则匹配
            k = str(GetTime.get_time(time_type[0], layout[0], unit[0]))
            value = re.sub(pattern, k, value, count=1)
    return value

