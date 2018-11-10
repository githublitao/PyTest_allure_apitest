#!/bin/bash
echo OFF

echo .:::::::::::::::::::::::::::::::::::::::::::::::::

echo .::                                           

echo .::                 接口测试                  

echo .::                                             

echo .::               作者： 李涛                 

echo .::                                            

echo .::               版本  V1.0.0               

echo .::                                              

echo .::               时间 2018.11.10              

echo .::                                          

echo .:::::::::::::::::::::::::::::::::::::::::::::::::

echo .[ INFO ] 运行环境准备

# 从配置文件中安装环境依赖库i
if [ -f requirements.txt ];
then
     pip install -r requirements.txt
fi
if [ ! -f requirements.txt ];
then
    echo requirements.txt does not exist
fi

echo .[INFO] 运行脚本
python3 main.py 
