# -*- coding:utf-8 -*-
import allure
import pytest
import yaml

from Common import init, check_result, requestSend

# 读取测试用例
with open("./test_zhongtai/test_smallNumber_bind_unbind/smallNumber.yaml", 'r', encoding="utf-8") as load_f:
    smalNumber_dict = yaml.load(load_f)

relevance = dict()


@allure.feature(smalNumber_dict["testinfo"]["title"])  # feature定义功能
class TestAddProject:
    def setup(self):
        global relevance
        relevance = init.ini_request(smalNumber_dict, relevance)

    # @pytest.mark.skipif(sys.version_info < (3, 6))  # 跳过条件
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
        code, data = requestSend.send_request(case_data, smalNumber_dict["testinfo"]["host"],
                                              smalNumber_dict["testinfo"]["address"], relevance)
        relevance = init.get_relevance(data, case_data["relevance"], relevance)
        # # 校验测试结果
        with allure.step("校验测试结果"):
            pass
        check_result.check(case_data["check"], code, data)
