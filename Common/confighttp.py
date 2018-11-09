# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 15:06

# @Author  : litao

# @Project : project

# @FileName: GetRelevance.py

# @Software: PyCharm

import json
import logging

import requests
import simplejson


def post(header, address, request_parameter_type, timeout=8, data=None, files=None):
    """
    post 请求
    :param header:  请求头
    :param address:  host地址
    :param request_parameter_type: 接口请求参数格式 （form-data, raw, Restful）
    :param timeout: 超时时间
    :param data: 请求参数
    :param files: 文件路径
    :return:
    """
    if request_parameter_type == 'raw':
        data = json.dumps(data)
    response = requests.post(url=address, data=data, headers=header, timeout=timeout, files=files)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def get(header, address, data, timeout=8):
    """
    get 请求
    :param header:  请求头
    :param address:  host地址
    :param data: 请求参数
    :param timeout: 超时时间
    :return:
    """
    response = requests.get(url=address, params=data, headers=header, timeout=timeout)
    if response.status_code == 301:
        response = requests.get(url=response.headers["location"])
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def put(header, address, request_parameter_type, data=None, timeout=8, files=None):
    """
    put 请求
    :param header:  请求头
    :param address:  host地址
    :param request_parameter_type: 接口请求参数格式 （form-data, raw, Restful）
    :param data: 请求参数
    :param timeout: 超时时间
    :param files: 文件路径
    :return:
    """
    if request_parameter_type == 'raw':
        data = json.dumps(data)
    response = requests.put(url=address, data=data, headers=header, timeout=timeout, files=files)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def delete(header, address, data, timeout=8):
    """
    put 请求
    :param header:  请求头
    :param address:  host地址
    :param timeout: 超时时间
    :param data: 请求参数
    :return:
    """
    response = requests.delete(url=address, params=data, headers=header, timeout=timeout)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise

