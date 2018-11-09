# -*- coding:utf-8 -*-
import os

import allure
import pytest
import yaml

from Common import init

# 读取测试用例
from Common.TestAndCheck import api_send_check

PATH = os.path.split(os.path.realpath(__file__))[0]
with open(PATH+"/Login.yaml", 'r', encoding="utf-8") as load_f:
    login_dict = yaml.load(load_f)

relevance = dict()


@allure.feature(login_dict["testinfo"]["title"])  # feature定义功能
class TestLogin:
    def setup(self):
        global relevance
        relevance = init.ini_request(login_dict, relevance)

    # @pytest.mark.skipif(fa)  # 跳过条件
    @pytest.mark.parametrize("case_data", login_dict["test_case"])
    @allure.story("登录")
    @allure.issue("http://www.baidu.com")  # bug地址
    @allure.testcase("http://www.testlink.com")  # 用例连接地址
    def test_login(self, case_data):
        """
        正常登陆   # 第一条用例描述
        :param case_data: 参数化用例的形参
        :return:
        """
        global relevance
        # 参数化修改test_login 注释
        for k, v in enumerate(login_dict["test_case"]):  # 遍历用例文件中所有用例的索引和值
            try:
                if case_data == v:
                    # 修改方法的__doc__在下一次调用时生效，此为展示在报告中的用例描述
                    TestLogin.test_login.__doc__ = login_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        relevance = api_send_check(case_data, login_dict, relevance)


if __name__ == "__main__":
    pytest.main("test_login.py")
