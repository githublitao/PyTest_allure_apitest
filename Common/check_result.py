import operator
import re

import allure

from Common import check_json

failureException = AssertionError


def check(case_data, code, data):
    """
    校验测试结果
    :param case_data:  测试用例
    :param code:  HTTP状态
    :param data:  返回的接口json数据
    :return:
    """
    # 不校验
    if case_data["check_type"] == 'no_check':
        with allure.step("不校验结果"):
            pass

    # 校验json格式
    elif case_data["check_type"] == 'json':
        with allure.step("JSON格式校验"):
            allure.attach("期望code", str(case_data["expected_code"]))
            allure.attach('期望data', str(case_data["expected_request"]))
        if int(code) == case_data["expected_code"]:
            if not data:
                data = "{}"
            check_json.check_json(case_data["expected_request"], data)
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 只校验HTTP状态
    elif case_data["check_type"] == 'only_check_status':
        with allure.step("校验HTTP状态"):
            allure.attach("期望code", str(case_data["expected_code"]))
        if int(code) == case_data["expected_code"]:
            pass
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 完全校验
    elif case_data["check_type"] == 'entirely_check':
        with allure.step("完全校验"):
            allure.attach("期望code", str(case_data["expected_code"]))
            allure.attach('期望data', str(case_data["expected_request"]))
        if int(code) == case_data["expected_code"]:
            result = operator.eq(case_data["expected_request"], data)
            if result:
                pass
            else:
                raise failureException("完全校验失败！ %s ! = %s" % (case_data["expected_request"], data))
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 正则校验
    elif case_data["check_type"] == 'Regular_check':
        with allure.step("正则校验"):
            allure.attach("期望code", str(case_data["expected_code"]))
            allure.attach('正则表达式', str(case_data["expected_request"]).replace("\'", "\""))
        if int(code) == case_data["expected_code"]:
            try:
                result = ""
                if isinstance(case_data["expected_request"], list):
                    for i in case_data["expected_request"]:
                        result = re.findall(i.replace("\"", "\'"), str(data))
                        allure.attach('校验完成结果', str(result))
                else:
                    result = re.findall(case_data["expected_request"].replace("\"", "\'"), str(data))
                    allure.attach('校验完成结果', str(result).replace("\'", "\""))
                if not result:
                    raise failureException("无正则校验内容！ %s" % case_data["expected_request"])
            except KeyError:
                raise failureException("正则校验执行失败！ %s" % case_data["expected_request"])
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 数据库校验
    elif case_data["check_type"] == "datebase_check":
        pass
    else:
        raise failureException("无该校验方式%s" % case_data["check_type"])
