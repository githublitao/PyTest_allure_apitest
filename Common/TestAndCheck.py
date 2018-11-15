# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 16:05

# @Author  : litao

# @Project : project

# @FileName: TestAndCheck.py

# @Software: PyCharm
import allure

from Common import requestSend, init, CheckResult


def api_send_check(case_data, project_dict, relevance, rel, _path, result):
    """
    接口请求并校验结果
    :param case_data:  单条用例
    :param project_dict:  用例文件对象
    :param relevance:  关联值实例对象
    :param _path:  case目录
    :param rel:  关联值类对象
    :param result:  全局测试结果
    :return:
    """
    # 发送请求并获取code， data
    code, data = requestSend.send_request(case_data, project_dict["testinfo"].get("host"),
                                          project_dict["testinfo"].get("address"), relevance, _path, result)
    # 校验测试结果
    with allure.step("校验测试结果"):
        pass
    if isinstance(case_data["check"], list):
        for i in case_data["check"]:
            CheckResult.check(case_data["test_name"], i, code, data, relevance, _path, result)
    else:
        CheckResult.check(case_data["test_name"], case_data["check"], code, data, relevance, _path, result)
    # 记录关联值
    init.get_relevance(data, case_data["relevance"], rel)


if __name__ == "__main__":
    path = 'D:\\project\\PyTest_allure_apitest\\test_case\\test_02_addProject'
    _case_data = {'test_name': '添加项目', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': [{'check_type': 'no_check', 'datebase': None, 'expected_code': None, 'expected_request': None, 'CustomFail': None}], 'relevance': ['王八大']}
    _project_dict = {'testinfo': {'id': 'test_addProject', 'title': '添加项目', 'host': '${test_platform}$', 'address': '/api/project/add_project'}, 'premise': [{'test_name': '登陆1', 'info': '正常登陆1', 'host': '${test_platform}$', 'address': '/api/user/login', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'form-data', 'headers': {}, 'timeout': 8, 'parameter': {'username': 'litao', 'password': 'lt19910301'}, 'file': False, 'relevance': ['key']}], 'test_case': [{'test_name': '添加项目', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': [{'check_type': 'no_check', 'datebase': None, 'expected_code': None, 'expected_request': None, 'CustomFail': None}], 'relevance': ['王八大']}, {'test_name': '添加项目1', 'info': '添加项目1', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '$RandomString(10)$ $RandomString(10)$', 'type': '$Choice(Web,App)list$', 'version': '$RandomInt(10,100)$ $RandomString(10)$', 'description': '$RandomFloat(10,100,5)$ $RandomString(10)$'}, 'file': False, 'check': [{'check_type': 'only_check_status', 'datebase': None, 'expected_code': 200, 'expected_request': None}], 'relevance': ['code']}, {'test_name': '添加项目2', 'info': '添加项目2', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '$GetTime(time_type=now,layout=%Y-%m,unit=5,5,5,5,5)$', 'type': 'Web', 'version': '321', 'description': '123'}, 'file': False, 'check': {'check_type': 'json', 'datebase': None, 'expected_code': 200, 'expected_request': {'code': '999997', 'msg': '存在相同名称', 'data': None}}, 'relevance': ['code']}, {'test_name': '添加项目3', 'info': '添加项目3', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': {'check_type': 'entirely_check', 'datebase': None, 'expected_code': 200, 'expected_request': {'code': '999997', 'msg': '存在相同名称', 'data': None}}, 'relevance': ['code']}, {'test_name': '添加项目4', 'info': '添加项目4', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': {'check_type': 'Regular_check', 'datebase': None, 'expected_code': 200, 'expected_request': ['存在相同名称', 'msg']}, 'relevance': ['code']}, {'test_name': '添加项目5', 'info': '添加项目5', 'http_type': 'http', 'request_type': 'post', 'parameter_type': 'raw', 'headers': {'Authorization': 'Token ${key}$', 'Content-Type': 'application/json'}, 'timeout': 8, 'parameter': {'name': '${name}$', 'type': '${type}$', 'version': '${version}$', 'description': '${description}$'}, 'file': False, 'check': {'check_type': 'datebase_check', 'datebase': {'name': 'api_test', 'user': 'root', 'password': 'lt19910301', 'port': 3306, 'sql': 'select * form api_test'}, 'expected_code': 200, 'expected_request': None}, 'relevance': ['code']}]}
    _rel = {'name': '9', 'type': 'Web', 'version': 'oKvtDG4Abd', 'description': 'oQDijtqUkr'}
    _relevance = {'name': '9', 'type': 'Web', 'version': 'oKvtDG4Abd', 'description': 'oQDijtqUkr', 'key': 'e1dfbfd759ad46bcdc44df989ade3f1c190cc936'}
    _result = {'result': True}
    api_send_check(_case_data, _project_dict, _relevance, _rel, path, _result)
