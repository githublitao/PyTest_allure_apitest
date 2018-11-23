# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm

import pytest
import allure
import requests

from config.configHost import ConfHost


@pytest.fixture(scope="session", autouse=True)
def env(request, run_env):
    """
    Parse env config info
    """
    host_config = ConfHost(run_env)
    host = host_config.get_host_conf()
    # allure.environment(app=host["TestEnv_app"])
    # allure.environment(微商城=host["TestEnv_wemall"])
    # allure.environment(官网=host["TestEnv_pc"])
    # allure.environment(正式环境访问域名v6_1=host["FormalEnv_v6_1"])
    # allure.environment(正式环境访问域名v6_11=host["FormalEnv_v6_11"])
    # allure.environment(正式环境访问域名v6_20=host["FormalEnv_v6_20"])
    # allure.environment(正式环境访问域名v6_22=host["FormalEnv_v6_22"])
    # allure.environment(正式环境访问域名v6_30=host["FormalEnv_v6_30"])
    # allure.environment(正式环境微商城=host["FormalEnv_wemall"])
    # allure.environment(正式环境官网=host["FormalEnv_pc"])
    # allure.environment(正式环境小程序=host["FormalEnv_applet"])


def pytest_addoption(parser):
    parser.addoption(
        "--RunEnv", action="store", default="TestHost",
        help="Run code in env"
    )
    parser.addoption(
        "--DatabaseEnv", action="store", default="TestDatabases",
        help="Database in env"
    )


@pytest.fixture(scope="session", autouse=True)
def run_env(request):
    return request.config.getoption("--RunEnv")


@pytest.fixture(scope="session", autouse=True)
def database_env(request):
    return request.config.getoption("--DatabaseEnv")

# @pytest.fixture(scope="session", autouse=True)
# def login(request):
#     # setup
#     url = "http://120.79.232.23/api/user/login"
#     parameter = {"username": "litao", "password": "lt19910301"}
#     response = requests.post(url=url, data=parameter)
#
#     def fin():
#         print("测试结束")
#     request.addfinalizer(fin)
#     return response.json()["token"]
#     yield
#     # teardown
#     print("测试完成")
#     print(response.json())
