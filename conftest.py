# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm
import random

import pytest
import allure
import requests

from config.configHost import ConfHost


@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    Parse env config info
    """
    host_config = ConfHost()
    host = host_config.get_host_conf()
    allure.environment(test_platform=host["test_platform"])
    allure.environment(mock=host["mock"])


@pytest.fixture(scope="session", autouse=True)
def login(request):
    # setup
    url = "http://120.79.232.23/api/user/login"
    parameter = {"username": "litao", "password": "lt19910301"}
    response = requests.post(url=url, data=parameter)
    yield
    # teardown
    print("测试完成")
    print(response.json())
