# -*- coding: utf-8 -*-

# @Time    : 2018/11/12 10:26

# @Author  : litao

# @Project : project

# @FileName: ConfigLogs.py

# @Software: PyCharm
import logging
import time

from Common.MkDir import mk_dir


class LogConfig:
    def __init__(self, path):
        """
        日志配置
        :param path: case 路径
        """
        runtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # Log等级总开关
        # 第二步，创建一个handler，用于写入全部日志文件
        mk_dir(path+"\logs\\")
        logfile = path + "\logs\\" + runtime + '.log'
        fh = logging.FileHandler(logfile, mode='w+')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 第三步，创建一个handler，用于写入错误日志文件
        logfile_error = path + "\logs\\" + runtime + '_error.log'
        fh_error = logging.FileHandler(logfile_error, mode='w+')
        fh_error.setLevel(logging.ERROR)  # 输出到file的log等级的开关
        # 第四步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
        # 第五步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        fh_error.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 第六步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(fh_error)
        logger.addHandler(ch)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=logfile,
                            filemode='w')
        logging.basicConfig(level=logging.ERROR,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=fh_error,
                            filemode='w')

