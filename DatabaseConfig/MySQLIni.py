# -*- coding: utf-8 -*-

# @Time    : 2018/11/16 14:59

# @Author  : litao

# @Project : project

# @FileName: MySQLIni.py

# @Software: PyCharm
import configparser
import os

import pymysql
from pymysql import ProgrammingError

from Exception.CustomException import NotFoundDatabase, DeficiencyDatabaseConfig, DatabaseConfigKeyError, \
    DatabaseSelectError

PATH = os.path.split(os.path.realpath(__file__))[0]


class MySQLConfig:
    # MySQL数据库初始化
    def __init__(self, env, db_name):
        config = configparser.ConfigParser()
        config.read(PATH + "/"+env+".ini", encoding="utf-8")
        try:
            database = config[db_name]
        except KeyError:
            raise NotFoundDatabase(db_name)
        try:
            host = database["host"]
            user = database["user"]
            password = database["password"]
            port = database["port"]
            db = database["db"]
        except KeyError as e:
            raise DeficiencyDatabaseConfig(db_name, e.args)
        if all([host, user, password, port, db, not isinstance(port, int)]):
            self.conn = self.get_conn(host, port, user, password, db)
        else:
            raise DatabaseConfigKeyError(db_name)

    @staticmethod
    def get_conn(host, port, user, password, db):
        config = {
            "host": host,
            "port": int(port),
            "user": user,
            "password": password,
            "database": db,
            "charset": "utf8"
        }
        conn = pymysql.connect(**config)
        return conn

    def select_sql(self, sql):
        cursor = self.conn.cursor()
        try:
            count = cursor.execute(sql)
        except ProgrammingError as e:
            raise DatabaseSelectError(sql, e)
        finally:
            cursor.close()
        return count


if __name__ == "__main__":
    mysql = MySQLConfig("TestDatabases", "plantform")
    print(mysql.select_sql('select * FROM api_test_project'))

