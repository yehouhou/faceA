# -*- coding:utf-8 -*-

"""
自定义异常类
"""

#寻找文件异常
class FileNotFounfdException(Exception):
    def __init__(self,err='找不到文件'):
        Exception.__init__(self,err)

#网络请求异常
class PicRequestException(Exception):
    def __init__(self,err='图片网络请求异常'):
        Exception.__init__(self,err)

"""
@author:raymond
@file:MyException.py
@time:2018/1/1611:44
"""