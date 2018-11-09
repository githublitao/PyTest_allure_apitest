# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm


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
    if isinstance(relevance_list, list):
        # 遍历关联键
        for j in relevance_list:
            # 从结果中提取关联键的值
            relevance_value = get_value(data, j)
            if relevance_value:
                # 考虑到一个关联键，多个值
                if j in relevance:
                    if isinstance(j, list):
                        a = relevance[j]
                        a.append(relevance_value)
                        relevance[j] = a
                    else:
                        a = relevance[j]
                        b = list()
                        b.append(a)
                        b.append(relevance_value)
                        relevance[j] = a
                else:
                    relevance[j] = relevance_value
    return relevance
