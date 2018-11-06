import allure

from Common.ParamManage import get_value
from Common.requestSend import send_request


def ini_request(case_dict, relevance):
    """

    :param case_dict: 用例对象
    :param relevance:  关联对象
    :return:
    """
    if isinstance(case_dict["premise"], list):
        with allure.step("接口关联请求"):
            for i in case_dict["premise"]:
                code, data = send_request(i, i["host"], i["address"], relevance)
                relevance = get_relevance(data, i["relevance"], relevance)
    return relevance


def get_relevance(data, relevance_list, relevance):
    """

    :param data:  返回结果
    :param relevance_list:  关联键列表
    :param relevance: 关联对象
    :return:
    """
    if isinstance(relevance_list, list):
        for j in relevance_list:
            relevance_value = get_value(data, j)
            if relevance_value:
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
