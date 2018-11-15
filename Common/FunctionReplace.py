# -*- coding: utf-8 -*-

# @Time    : 2018/11/11 17:07

# @Author  : litao

# @Project : project

# @FileName: FunctionReplace.py

# @Software: PyCharm
import re

from RandomData import RandomString, RandomInt, GetTime, ChoiceData, RandomFloat, Md5Data


def function_replace(value):
    """
    调用定义方法替换字符串
    :param value:
    :return:
    """
    int_list = re.findall('\$RandomInt\(([0-9]*,[0-9]*?)\)\$', value)
    string_list = re.findall('\$RandomString\(([0-9]*?)\)\$', value)
    float_list = re.findall("\$RandomFloat\(([0-9]*,[0-9]*,[0-9]*)\)\$", value)
    time_list = re.findall("\$GetTime\(time_type=(.*?),layout=(.*?),unit=([0-9],[0-9],[0-9],[0-9],[0-9])\)\$", value)
    choice_list = re.findall("\$Choice\(((?!\$Choice\().*?)\)list\$", value)
    if len(int_list):
        # 获取整型数据替换
        for i in int_list:
            pattern = re.compile('\$RandomInt\(' + i + '\)\$')  # 初始化正则匹配
            k = str(RandomInt.random_int(i))
            value = re.sub(pattern, k, value, count=1)
        value = function_replace(value)
    elif len(string_list):
        # 获取字符串替换
        for j in string_list:
            pattern = re.compile('\$RandomString\(' + j + '\)\$')  # 初始化正则匹配
            k = RandomString.random_string(j)
            value = re.sub(pattern, k, value, count=1)
        value = function_replace(value)
    elif len(float_list):
        # 获取浮点数
        for n in float_list:
            if len(n.split(",")) == 3:
                pattern = re.compile('\$RandomFloat\(' + n + '\)\$')  # 初始化正则匹配
                k = str(RandomFloat.random_float(n))
                value = re.sub(pattern, k, value, count=1)
        value = function_replace(value)
    elif len(time_list):
        # 获取时间替换
        for n in time_list:
            if len(n[0]) and len(n[1]):
                pattern = re.compile('\$GetTime\(time_type='+n[0]+',layout='+n[1]+',unit='+n[2]+'\)\$')  # 初始化正则匹配
                k = str(GetTime.get_time(n[0], n[1], n[2]))
                value = re.sub(pattern, k, value, count=1)
        value = function_replace(value)
    elif len(choice_list):
        # 调用choice方法
        for n in choice_list:
            pattern = re.compile('\$Choice\(' + n + '\)list\$')  # 初始化正则匹配
            k = str(ChoiceData.choice_data(n))
            value = re.sub(pattern, k, value, count=1)
        value = function_replace(value)
    else:
        # md5加密
        value = Md5Data.re_md5(value)
    return value


if __name__ == '__main__':
    int_num = '$RandomInt($RandomInt($RandomInt(1,11)$,$RandomInt(2,12)$)$,$RandomInt($RandomInt(3,13)$,$RandomInt(4,14)$)$)$' \
              '$RandomInt($RandomInt($RandomInt(5,15)$,$RandomInt(6,16)$)$,$RandomInt($RandomInt(7,17)$,$RandomInt(8,18)$)$)$'
    float_num = '$RandomFloat($RandomInt(1,11)$,$RandomInt(1,11)$,$RandomInt(1,11)$)$'
    string_num = '$RandomString($RandomInt($RandomInt(1,11)$,$RandomInt(2,12)$)$)$'
    time_num = '$GetTime(time_type=now,layout=13timestamp,unit=5,5,5,5,5)$'
    choice_num = '$RandomInt($Choice($Choice(' + int_num + ',' + int_num + ',' + int_num + ',' + int_num + \
                 ')list$)list$,$Choice($Choice(' + int_num + ',' + int_num + ',' + int_num + ',' + int_num + ')list$)list$)$'
    print(function_replace(int_num))
    print(function_replace(string_num))
    print(function_replace(time_num))
    print(function_replace(float_num))
    print(function_replace(choice_num))
