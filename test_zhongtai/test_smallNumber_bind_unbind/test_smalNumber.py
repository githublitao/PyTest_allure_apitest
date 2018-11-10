# -*- coding:utf-8 -*-
import os

import allure
import pytest

from Common import init

# 读取测试用例
from Common.IniCase import ini_case
from Common.TestAndCheck import api_send_check


PATH = os.path.split(os.path.realpath(__file__))[0]
case_dict, relevance = ini_case(PATH)


@allure.feature(case_dict["testinfo"]["title"])  # feature定义功能
class TestAddProject:
    def setup(self):
        global relevance
        relevance = init.ini_request(case_dict, relevance, PATH)

    @pytest.mark.parametrize("case_data", case_dict["test_case"])
    @allure.story("小号绑定/解绑")
    def test_add_project(self, case_data):
        """
        按订单号绑定
        :param case_data:
        :return:
        """
        global relevance
        # 参数化修改test_login 注释
        for k, v in enumerate(case_dict["test_case"]):
            try:
                if case_data == v:
                    TestAddProject.test_add_project.__doc__ = case_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        # 发送测试请求
        relevance = api_send_check(case_data, case_dict, relevance, PATH)


if __name__ == "__main__":
    pytest.main()
