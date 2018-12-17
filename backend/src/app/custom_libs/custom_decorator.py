#!/usr/bin/env python2.7
# encoding: utf-8
"""=======================================

    company : Dilusense
     author : Kuangch
       date : 2018/6/2

======================================="""
import functools, traceback
from flask import json
from routes import logger_main
from services.cache.data_cache import DataCache


def hand_request_exception(msg='server inner error'):
    """
    flask 请求异常处理
    """

    def hand_request_exception_decorator(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                logger_main.error(traceback.format_exc())
                return json.dumps({'code': -1, 'msg': msg})

        return wrapper

    return hand_request_exception_decorator


request_cache = DataCache()


def request_interval_control(time=3):
    """
    flask 请求间隔时间控制
    """

    def request_interval_control_decorator(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if request_cache.is_obsolete(f.func_name,duration=time):
                request_cache.update(f.func_name, '')
                return f(*args, **kwargs)
            else:
                return json.dumps({'code': -1000, 'msg': '特殊请求,两次请求需要间隔%d秒'%time,'interval': time})

        return wrapper

    return request_interval_control_decorator