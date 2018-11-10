# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 16:05

# @Author  : litao

# @Project : project

# @FileName: TestAndCheck.py

# @Software: PyCharm
import allure

from Common import requestSend, init, CheckResult


def api_send_check(case_data, project_dict, relevance, _path):
    """
    接口请求并校验结果
    :param case_data:  单条用例
    :param project_dict:  用例文件对象
    :param relevance:  关联值对象
    :param _path:  case目录
    :return:  关联值对象
    """
    # 发送请求并获取code， data
    code, data = requestSend.send_request(case_data, project_dict["testinfo"].get("host"),
                                          project_dict["testinfo"].get("address"), relevance, _path)
    # 校验测试结果
    with allure.step("校验测试结果"):
        pass
    if isinstance(case_data["check"], list):
        for i in case_data["check"]:
            CheckResult.check(case_data["test_name"], i, code, data, relevance, _path)
    else:
        CheckResult.check(case_data["test_name"], case_data["check"], code, data, relevance, _path)
    # 记录关联值
    relevance = init.get_relevance(data, case_data["relevance"], relevance)
    return relevance
