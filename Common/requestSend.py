# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import logging

import allure

from Common import confighttp, HostManage, ReadParam, ParamManage
from main import failureException


def send_request(data, host, address, relevance, _path, success):
    """
    再次封装请求
    :param data: 测试用例
    :param host: 测试地址
    :param address: 接口地址
    :param relevance: 关联对象
    :param _path: case路径
    :param success: 全局结果
    :return:
    """
    logging.info("="*100)
    header = ReadParam.read_param(data["test_name"], data["headers"], relevance, _path, success)  # 处理请求头
    logging.debug("请求头处理结果：  %s" % header)
    parameter = ReadParam.read_param(data["test_name"], data["parameter"], relevance, _path, success)  # 处理请求参数
    logging.debug("请求参数处理结果：  %s" % header)
    try:
        # 如果用例中写了host和address，则使用用例中的host和address，若没有则使用全局的
        host = data["host"]
    except KeyError:
        pass
    try:
        address = data["address"]
    except KeyError:
        pass
    host = HostManage.host_manage(host)  # host处理，读取配置文件中的host
    address = ParamManage.manage(address, relevance)
    logging.debug("host处理结果：  %s" % host)
    if not host:
        raise failureException("接口请求地址为空  %s" % data["headers"])
    logging.info("请求接口：%s" % str(data["test_name"]))
    logging.info("请求地址：%s" % data["http_type"] + "://" + host + address)
    logging.info("请求头: %s" % str(header))
    logging.info("请求参数: %s" % str(parameter))
    if data["request_type"].lower() == 'post':
        if data["file"]:
            with allure.step("POST上传文件"):
                allure.attach("请求接口：", str(data["test_name"]))
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            result = confighttp.post(header=header,
                                     address=data["http_type"] + "://" + host + address,
                                     request_parameter_type=data["parameter_type"], files=parameter,
                                     timeout=data["timeout"])
        else:
            with allure.step("POST请求接口"):
                allure.attach("请求接口：", str(data["test_name"]))
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            logging.info("POST请求接口")
            result = confighttp.post(header=header, address=data["http_type"] + "://" + host + address,
                                     request_parameter_type=data["parameter_type"], data=parameter,
                                     timeout=data["timeout"])
    elif data["request_type"].lower() == 'get':
        with allure.step("GET请求接口"):
            allure.attach("请求接口：", str(data["test_name"]))
            allure.attach("请求地址", data["http_type"] + "://" + host + address)
            allure.attach("请求头", str(header))
            allure.attach("请求参数", str(parameter))
        logging.info("GET请求接口")
        result = confighttp.get(header=header, address=data["http_type"] + "://" + host + address,
                                data=parameter, timeout=data["timeout"])
    elif data["request_type"].lower() == "put":
        if data["file"]:
            with allure.step("PUT上传文件"):
                allure.attach("请求接口：", str(data["test_name"]))
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            logging.info("PUT上传文件")
            result = confighttp.put(header=header,
                                    address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"], files=parameter,
                                    timeout=data["timeout"])
        else:
            with allure.step("PUT请求接口"):
                allure.attach("请求接口：", str(data["test_name"]))
                allure.attach("请求地址", data["http_type"] + "://" + host + address)
                allure.attach("请求头", str(header))
                allure.attach("请求参数", str(parameter))
            logging.info("PUT请求接口")
            result = confighttp.put(header=header, address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"], data=parameter,
                                    timeout=data["timeout"])
    elif data["request_type"].lower() == "delete":
        with allure.step("DELETE请求接口"):
            allure.attach("请求接口：", str(data["test_name"]))
            allure.attach("请求地址", data["http_type"] + "://" + host + address)
            allure.attach("请求头", str(header))
            allure.attach("请求参数", str(parameter))
        logging.info("DELETE请求接口")
        result = confighttp.delete(header=header, address=data["http_type"] + "://" + host + address,
                                   data=parameter, timeout=data["timeout"])
    else:
        result = {"code": False, "data": False}
    logging.info("接口请求结果：\n %s" % str(result))
    return result


if __name__ == "__main__":
    path = 'D:\\project\\PyTest_allure_apitest\\test_case\\test_02_addProject'
    _address = '/api/project/add_project'
    _data = {'test_name': '登陆1', 'info': '正常登陆1', 'host': '${test_platform}$', 'address': '/api/user/login', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'form-data', 'headers': {}, 'timeout': 8, 'parameter': {'username': 'litao', 'password': 'lt19910301'}, 'file': False, 'relevance': ['key']}
    _host = '${test_platform}$'
    _relevance = {'name': '9', 'type': 'Web', 'version': 'ByTQF7Zmaz', 'description': 'V7GeXKU9E6'}
    _success = {'result': True}
    print(send_request(_data, _host, _address, _relevance, path, _success))
