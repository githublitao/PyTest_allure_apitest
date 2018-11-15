# -*- coding:utf-8 -*-
import os

import allure
import pytest

from Common import init

# 读取测试用例
from Common.IniCase import ini_case
from Common.IniRelevance import ini_relevance
from Common.TestAndCheck import api_send_check
from config.ConfigLogs import LogConfig

PATH = os.path.split(os.path.realpath(__file__))[0]

case_dict = ini_case(PATH)


@allure.feature(case_dict["testinfo"]["title"])  # feature定义功能
class TestAddProject:

    @classmethod
    def setup_class(cls):
        cls.rel = ini_relevance(PATH)
        cls.result = {"result": True}

    def setup(self):
        self.relevance = self.rel.copy()
        self.relevance = init.ini_request(case_dict, self.relevance, PATH, self.result)

    @pytest.mark.parametrize("case_data", case_dict["test_case"])
    @allure.story("小号绑定/解绑")
    def test_add_project(self, case_data):
        """
        按订单号绑定
        :param case_data:
        :return:
        """
        # 参数化修改test_login 注释
        for k, v in enumerate(case_dict["test_case"]):
            try:
                if case_data == v:
                    TestAddProject.test_add_project.__doc__ = case_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        # 发送测试请求
        api_send_check(case_data, case_dict,  self.relevance, self.rel,  PATH, self.result)


if __name__ == "__main__":
    LogConfig(PATH)
    pytest.main()
