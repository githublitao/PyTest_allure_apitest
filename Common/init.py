# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import logging
import time

import allure

from Common.GetRelevance import get_relevance
from Common.requestSend import send_request
from main import failureException


def ini_request(case_dict, relevance, _path, result):
    """
    用例前提条件执行，提取关联键
    :param case_dict: 用例对象
    :param relevance:  关联对象
    :param _path:  case路径
    :param result:  全局结果
    :return:
    """
    if isinstance(case_dict["premise"], list):
        logging.info("执行测试用例前置接口")
        with allure.step("接口关联请求"):
            for i in case_dict["premise"]:
                relevance_list = relevance.copy()
                for j in range(0, 3):
                    # 获取前置接口关联数据失败
                    code, data = send_request(i, case_dict["testinfo"].get("host"),
                                              case_dict["testinfo"].get("address"), relevance_list, _path, result)
                    if not data:
                        with allure.step("接口请求失败！等待三秒后重试！"):
                            pass
                        logging.info("接口请求失败！等待三秒后重试！")
                        continue
                    if i["relevance"]:
                        if len(i["relevance"]):
                            relevance = get_relevance(data, i["relevance"], relevance)
                            if isinstance(relevance, bool):
                                with allure.step("从结果中提取关联键的值失败！等待3秒后重试！"):
                                    pass
                                logging.info("从结果中提取关联键的值失败！等待3秒后重试！")
                                time.sleep(3)
                                continue
                            else:
                                break
                        else:
                            break
                    else:
                        break
                if isinstance(relevance, bool):
                    logging.info("从结果中提取关联键的值失败！重试三次失败")
                    result["result"] = False
                    raise failureException("获取前置接口关联数据失败")
    return relevance


if __name__ == "__main__":
    path = 'D:\\project\\PyTest_allure_apitest\\test_case\\test_02_addProject'
    _case_dict = {'testinfo': {'id': 'test_addProject', 'title': '添加项目', 'host': '${test_platform}$', 'address': '/api/project/add_project'}, 'premise': [{'test_name': '登陆1', 'info': '正常登陆1', 'host': '${test_platform}$', 'address': '/api/user/login', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'form-data', 'headers': {}, 'timeout': 8, 'parameter': {'username': 'litao', 'password': 'lt19910301'}, 'file': False, 'relevance': ['key']}], 'test_case': [{'test_name': '添加项目', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': [{'check_type': 'no_check', 'datebase': None, 'expected_code': None, 'expected_request': None, 'CustomFail': None}], 'relevance': ['王八大']}, {'test_name': '添加项目1', 'info': '添加项目1', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '$RandomString(10)$ $RandomString(10)$', 'type': '$Choice(Web,App)list$', 'version': '$RandomInt(10,100)$ $RandomString(10)$', 'description': '$RandomFloat(10,100,5)$ $RandomString(10)$'}, 'file': False, 'check': [{'check_type': 'only_check_status', 'datebase': None, 'expected_code': 200, 'expected_request': None}], 'relevance': ['code']}, {'test_name': '添加项目2', 'info': '添加项目2', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '$GetTime(time_type=now,layout=%Y-%m,unit=5,5,5,5,5)$', 'type': 'Web', 'version': '321', 'description': '123'}, 'file': False, 'check': {'check_type': 'json', 'datebase': None, 'expected_code': 200, 'expected_request': {'code': '999997', 'msg': '存在相同名称', 'data': None}}, 'relevance': ['code']}, {'test_name': '添加项目3', 'info': '添加项目3', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': {'check_type': 'entirely_check', 'datebase': None, 'expected_code': 200, 'expected_request': {'code': '999997', 'msg': '存在相同名称', 'data': None}}, 'relevance': ['code']}, {'test_name': '添加项目4', 'info': '添加项目4', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': {'check_type': 'Regular_check', 'datebase': None, 'expected_code': 200, 'expected_request': ['存在相同名称', 'msg']}, 'relevance': ['code']}, {'test_name': '添加项目5', 'info': '添加项目5', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': {'check_type': 'datebase_check', 'datebase': {'name': 'api_test', 'user': 'root', 'password': 'lt19910301', 'port': 3306, 'sql': 'select * form api_test'}, 'expected_code': 200, 'expected_request': None}, 'relevance': ['code']}]}
    _relevance = {'name': '2', 'type': 'Web', 'version': '7m8uPQOXaz', 'description': 'A038mj4sqv'}
    _result = {'result': True}
    print(ini_request(_case_dict, _relevance, path, _result))

