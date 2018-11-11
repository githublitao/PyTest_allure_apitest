# -*- coding:utf-8 -*-
import os

import allure
import pytest

from Common import init

# 读取测试用例
from Common.IniCase import ini_case
from Common.IniRelevance import ini_relevance
from Common.TestAndCheck import api_send_check

PATH = os.path.split(os.path.realpath(__file__))[0]


case_dict = ini_case(PATH)


@allure.feature(case_dict["testinfo"]["title"])  # feature定义功能
class TestAddProject:
    def setup(self):
        self.relevance = ini_relevance(PATH)
        self.relevance = init.ini_request(case_dict, self.relevance, PATH)

    # @pytest.mark.skipif(sys.version_info < (3, 6))  # 跳过条件
    @pytest.mark.parametrize("case_data", case_dict["test_case"])
    @allure.story("添加项目")
    @allure.issue("http://www.baidu.com")  # bug地址
    @allure.testcase("http://www.testlink.com")  # 用例连接地址
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_add_project(self, case_data):
        """
        添加项目测试  # 第一条用例描述
        :param case_data: 参数化用例的形参
        :return:
        """
        # 参数化修改test_add_project 注释
        for k, v in enumerate(case_dict["test_case"]): # 遍历用例文件中所有用例的索引和值
            try:
                if case_data == v:
                    # 修改方法的__doc__在下一次调用时生效，此为展示在报告中的用例描述
                    TestAddProject.test_add_project.__doc__ = case_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        # 发送测试请求
        api_send_check(case_data, case_dict, self.relevance, PATH)


if __name__ == "__main__":
    pytest.main()
