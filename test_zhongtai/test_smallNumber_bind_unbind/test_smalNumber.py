# -*- coding:utf-8 -*-
import os

import allure
import pytest
import yaml

from Common import init

# 读取测试用例
from Common.TestAndCheck import api_send_check


PATH = os.path.split(os.path.realpath(__file__))[0]
with open(PATH+"/smallNumber.yaml", 'r', encoding="utf-8") as load_f:
    smalNumber_dict = yaml.load(load_f)

relevance = dict()


@allure.feature(smalNumber_dict["testinfo"]["title"])  # feature定义功能
class TestAddProject:
    def setup(self):
        global relevance
        relevance = init.ini_request(smalNumber_dict, relevance)

    @pytest.mark.parametrize("case_data", smalNumber_dict["test_case"])
    @allure.story("小号绑定/解绑")
    def test_add_project(self, case_data):
        """
        按订单号绑定
        :param case_data:
        :return:
        """
        global relevance
        # 参数化修改test_login 注释
        for k, v in enumerate(smalNumber_dict["test_case"]):
            try:
                if case_data == v:
                    TestAddProject.test_add_project.__doc__ = smalNumber_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        # 发送测试请求
        relevance = api_send_check(case_data, smalNumber_dict, relevance)


if __name__ == "__main__":
    pytest.main()