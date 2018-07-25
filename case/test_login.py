# -*- coding:utf-8 -*-
import json
import allure
import pytest

from Common.check_result import check
from Common.requestSend import send_request


# 读取测试用例
with open("./case/Login.json", 'r', encoding="utf-8") as load_f:
    login_dict = json.load(load_f)


@allure.feature('登录')  # feature定义功能
class TestLogin:

    @pytest.mark.parametrize("case_data", login_dict)
    @allure.story("登录")
    def test_login(self, case_data):
        # 发送测试请求
        code, data = send_request(case_data)
        # # 校验测试结果
        with allure.step("校验测试结果"):
            pass
        check(case_data, code, data)


