# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 20:57

# @Author  : litao

# @Project : project

# @FileName: CustomFail.py

# @Software: PyCharm
import re


def custom_manage(custom_fail, relevance):
    """
    自定义关联配置
    :param custom_fail:  自定义错误说明
    :param relevance:  关联对象
    :return:
    """
    try:
        relevance_list = re.findall("\${(.*?)}\$", custom_fail)  # 查找字符串中所有$key$ 作为关联对象
        for n in relevance_list:  # 遍历关联key
            pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
            custom_fail = re.sub(pattern, relevance[n], custom_fail, count=1)  # 关联值1次
    except TypeError:
        pass
    return custom_fail


if __name__ == "__main__":
    _custom_fail = "这是一段${test}$用的数据"
    _relevance = {"test": "测试"}
    print(custom_manage(_custom_fail, _relevance))

