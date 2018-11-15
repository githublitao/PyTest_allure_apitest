# -*- coding: utf-8 -*-

# @Time    : 2018/11/11 10:58

# @Author  : litao

# @Project : project

# @FileName: RandomFloat.py

# @Software: PyCharm

import random

from main import failureException


def random_float(data):
    """
    获取随机整型数据
    :param data:
    :return:
    """
    try:
        start_num, end_num, accuracy = data.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
        accuracy = int(accuracy)
    except ValueError:
        raise failureException("调用随机整数失败，范围参数或精度有误！\n小数范围精度 %s" % data)
    if start_num <= end_num:
        num = random.uniform(start_num, end_num)
    else:
        num = random.uniform(end_num, start_num)
    num = round(num, accuracy)
    return num


if __name__ == "__main__":
    print(random_float("200, 100, 5"))
