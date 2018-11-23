# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 20:08

# @Author  : litao

# @Project : project

# @FileName: ConfRelevance.py

# @Software: PyCharm
#   自定义异常类，可自行添加


class NotFoundDatabase(Exception):
    def __init__(self, name):
        err = '未通过数据库名称 "{0}" 找到对应配置信息'.format(name)
        Exception.__init__(self, err)


class DeficiencyDatabaseConfig(Exception):
    def __init__(self, name, data):
        err = '数据库 "{0}" 配置信息配置缺失  {1}'.format(name, data)
        Exception.__init__(self, err)


class CaseNotFound(Exception):
    def __init__(self, code_json):
        err = '用例关联文件不存在\n文件路径： {0}'.format(code_json)
        Exception.__init__(self, err)


class CaseRelevanceFileFormatError(Exception):
    def __init__(self, code_json):
        err = '用例关联的期望文件格式有误\n文件路径： {0}'.format(code_json)
        Exception.__init__(self, err)


class CaseRelevanceIndexNotFound(Exception):
    def __init__(self, code_json, test_name):
        err = '未找到用例关联的期望结果\n文件路径： {0}\n索引： {1}'.format(code_json, test_name)
        Exception.__init__(self, err)


class GetPremiseRelevanceError(Exception):
    def __init__(self):
        err = "获取前置接口关联数据失败"
        Exception.__init__(self, err)


class DatabaseConfigKeyError(Exception):
    def __init__(self, name):
        err = '数据库"{0}"配置文件参数有误'.format(name)
        Exception.__init__(self, err)


class DatabaseSelectError(Exception):
    def __init__(self, name, e):
        err = '数据库查询失败, SQL: {0}\n {1}'.format(name, e)
        Exception.__init__(self, err)


class CaseDatabaseConfigError(Exception):
    def __init__(self, e):
        err = '用例数据库校验配置有误！  {0}'.format(e)
        Exception.__init__(self, err)


class RelevanceFormatError(Exception):
    def __init__(self, relevance):
        err = '用例关联输入有误！  {0}'.format(relevance)
        Exception.__init__(self, err)


class RelevanceIndexError(Exception):
    def __init__(self, relevance, n):
        err = '关联值替换时超出索引！  {0}\n {1}'.format(relevance, n)
        Exception.__init__(self, err)


class RelevanceIndexNotInt(Exception):
    def __init__(self, n):
        err = '关联值索引填写非整型！  {0}'.format(n)
        Exception.__init__(self, err)


class RelevanceValueError(Exception):
    def __init__(self, n):
        err = '关联值填写有误！  {0}'.format(n)
        Exception.__init__(self, err)
