# -*- coding:utf-8 -*-
import allure
import pytest
import yaml

from Common import init, check_result, requestSend

# 读取测试用例
with open("./test_case/test_02_addProject/project.yaml", 'r', encoding="utf-8") as load_f:
    project_dict = yaml.load(load_f)

relevance = dict()


@allure.feature(project_dict["testinfo"]["title"])  # feature定义功能
class TestAddProject:
    def setup(self):
        global relevance
        relevance = init.ini_request(project_dict, relevance)

    @pytest.mark.parametrize("case_data", project_dict["test_case"])
    @allure.story("添加项目")
    def test_add_project(self, case_data):
        """
        添加项目测试
        :param case_data:
        :return:
        """
        global relevance
        # 参数化修改test_login 注释
        for k, v in enumerate(project_dict["test_case"]):
            try:
                if case_data == v:
                    TestAddProject.test_add_project.__doc__ = project_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        # 发送测试请求
        code, data = requestSend.send_request(case_data, project_dict["testinfo"]["host"],
                                              project_dict["testinfo"]["address"], relevance)
        relevance = init.get_relevance(data, case_data["relevance"], relevance)
        # # 校验测试结果
        with allure.step("校验测试结果"):
            pass
        check_result.check(case_data["check"], code, data)


