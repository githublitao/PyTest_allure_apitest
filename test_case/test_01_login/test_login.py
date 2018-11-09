# -*- coding:utf-8 -*-

import allure
import pytest
import yaml

from Common import requestSend, check_result, init

# 读取测试用例
with open("./test_case/test_01_login/Login.yaml", 'r', encoding="utf-8") as load_f:
    login_dict = yaml.load(load_f)

relevance = dict()


@allure.feature(login_dict["testinfo"]["title"])  # feature定义功能
class TestLogin:
    def setup(self):
        self.relevance = init.ini_request(login_dict, relevance)

    # @pytest.mark.skipif(fa)  # 跳过条件
    @pytest.mark.parametrize("case_data", login_dict["test_case"])
    @allure.story("登录")
    @allure.issue("http://www.baidu.com")  # bug地址
    @allure.testcase("http://www.testlink.com")  # 用例连接地址
    def test_login(self, case_data):
        """
        正常登陆
        :param case_data:
        :return:
        """
        # 参数化修改test_login 注释
        for k, v in enumerate(login_dict["test_case"]):
            try:
                if case_data == v:
                    TestLogin.test_login.__doc__ = login_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        # 发送测试请求
        code, data = requestSend.send_request(case_data, login_dict["testinfo"]["host"],
                                              login_dict["testinfo"]["address"], relevance)
        with allure.step("校验测试结果"):
            pass
        check_result.check(case_data["check"], code, data)


if __name__ == "__main__":
    pytest.main("test_login")
