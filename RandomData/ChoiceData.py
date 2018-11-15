# -*- coding: utf-8 -*-

# @Time    : 2018/11/12 19:22

# @Author  : litao

# @Project : project

# @FileName: ChoiceData.py

# @Software: PyCharm
import random


def choice_data(data):
    """
    获取随机整型数据
    :param data:
    :return:
    """
    _list = data.split(",")
    num = random.choice(_list)
    return num


if __name__ == "__main__":
    print(choice_data("200, 100, 5"))
