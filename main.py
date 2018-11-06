# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
# coding:utf-8
import os

import pytest

case_path = os.path.join(os.getcwd())

if __name__ == '__main__':
    pytest.main("--alluredir report")
    # pytest.main()
    os.popen("allure generate report/ -o result/ --clean")
    os.popen("allure open -h 127.0.0.1 -p 8083 result/")
