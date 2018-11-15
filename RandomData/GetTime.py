# -*- coding: utf-8 -*-

# @Time    : 2018/11/11 11:33

# @Author  : litao

# @Project : project

# @FileName: GetTime.py

# @Software: PyCharm
import datetime
import time

from main import failureException


def get_time(time_type, layout, unit="0,0,0,0,0"):
    """
    获取时间
    :param time_type: 现在的时间now， 其他时间else_time
    :param layout: 10timestamp， 13timestamp,  else  时间类型
    :param unit: 时间单位： [seconds, minutes, hours, days, weeks] 秒，分，时，天，周
    :return:
    """
    tim = datetime.datetime.now()
    if time_type != "now":
        lag = unit.split(",")
        try:
            tim = tim + datetime.timedelta(seconds=int(lag[0]), minutes=int(lag[1]),
                                           hours=int(lag[2]), days=int(lag[3]), weeks=int(lag[4]))
        except ValueError:
            raise failureException("获取时间错误，时间单位%s" % unit)
    # 获取10位时间戳
    if layout == "10timestamp":
        tim = tim.strftime('%Y-%m-%d %H:%M:%S')
        tim = int(time.mktime(time.strptime(tim, "%Y-%m-%d %H:%M:%S")))
        return tim
    # 获取13位时间戳
    elif layout == "13timestamp":
        tim = tim.strftime('%Y-%m-%d %H:%M:%S')
        tim = int(time.mktime(time.strptime(tim, "%Y-%m-%d %H:%M:%S")))
        tim = int(round(tim * 1000))
        return tim
    # 按传入格式获取时间
    else:
        tim = tim.strftime(layout)
        return tim


if __name__ == "__main__":
    print(get_time("else_time", "%Y-%m-%d %H:%M:%S", "5,5,5,5,5"))
    print(get_time("now", "%Y-%m-%d %H:%M:%S", "5,5,5,5,5"))

