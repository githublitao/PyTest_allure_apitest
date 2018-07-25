import allure

from Common.confighttp import post, get, put, delete


def send_request(data):
    """
    再次封装请求
    :param data: 测试用例
    :return:
    """
    if data["request_type"] == 'post':
        if data["file"]:
            with allure.step("POST上传文件"):
                allure.attach("请求地址", data["http_type"] + "://" + data["host"] + data["address"])
                allure.attach("请求头", str(data["headers"]))
                allure.attach("请求参数", str(data["parameter"]))
            result = post(header=data["headers"],
                          address=data["http_type"] + "://" + data["host"] + data["address"],
                          request_parameter_type=data["parameter_type"], files=data["parameter"],
                          timeout=data["timeout"])
        else:
            with allure.step("POST请求接口"):
                allure.attach("请求地址", data["http_type"] + "://" + data["host"] + data["address"])
                allure.attach("请求头", str(data["headers"]))
                allure.attach("请求参数", str(data["parameter"]))
            result = post(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                          request_parameter_type=data["parameter_type"], data=data["parameter"],
                          timeout=data["timeout"])
    elif data["request_type"] == 'get':
        with allure.step("GET请求接口"):
            allure.attach("请求地址", data["http_type"] + "://" + data["host"] + data["address"])
            allure.attach("请求头", str(data["headers"]))
            allure.attach("请求参数", str(data["parameter"]))
        result = get(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                     data=data["parameter"], timeout=data["timeout"])
    elif data["request_type"] == "put":
        if data["file"]:
            with allure.step("PUT上传文件"):
                allure.attach("请求地址", data["http_type"] + "://" + data["host"] + data["address"])
                allure.attach("请求头", str(data["headers"]))
                allure.attach("请求参数", str(data["parameter"]))
            result = put(header=data["headers"],
                         address=data["http_type"] + "://" + data["host"] + data["address"],
                         request_parameter_type=data["parameter_type"], files=data["parameter"],
                         timeout=data["timeout"])
        else:
            with allure.step("PUT请求接口"):
                allure.attach("请求地址", data["http_type"] + "://" + data["host"] + data["address"])
                allure.attach("请求头", str(data["headers"]))
                allure.attach("请求参数", str(data["parameter"]))
            result = put(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                         request_parameter_type=data["parameter_type"], data=data["parameter"],
                         timeout=data["timeout"])
    elif data["request_type"] == "delete":
        with allure.step("DELETE请求接口"):
            allure.attach("请求地址", data["http_type"] + "://" + data["host"] + data["address"])
            allure.attach("请求头", str(data["headers"]))
            allure.attach("请求参数", str(data["parameter"]))
        result = delete(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                        data=data["parameter"], timeout=data["timeout"])
    else:
        return False, False
    return result
