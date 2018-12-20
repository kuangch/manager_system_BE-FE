#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all api is for frontend interface
import traceback
from flask import json, make_response, session, request
from custom_libs.custom_decorator import hand_request_exception
from flask_application import app, logger_main
from utils.global_info import GlobalInfo
from utils.my_constant import MyConstant


@app.before_request
def login_check():

    # 每个请求前进行登录校验
    if request.path not in [
        # 排除登录校验的path
        '/login',
        '/logout'
    ] and 'username' not in session:

        response = make_response(json.dumps({
            'code': 1001,
            'msg': "未登录"
        }), 401)
        return response


@app.route('/login')
@hand_request_exception()
def login():

    response = make_response(json.dumps({
        'code': 0,
        'msg': '登录成功'
    }))
    session['username'] = 'kuangch'

    from datetime import timedelta

    try:
        login_status_time = int(float(GlobalInfo.login_status_lifetime) * 60)
    except:
        # 默认5分钟
        login_status_time = MyConstant.web_config_login_status_lifetime_default * 60
        logger_main.error(traceback.format_exc())

    logger_main.debug('登录状态保持时间: %d秒', login_status_time)

    # 设置session过期时间
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=login_status_time)

    return response


@app.route('/logout')
@hand_request_exception()
def logout():

    response = make_response(json.dumps({
        'code': 0,
        'msg': '退出登录成'
    }))

    if 'username' in session:
        logger_main.debug('logout')
        session.pop('username')

    return response


@app.route('/loginVerify')
@hand_request_exception()
def login_verify():

    # 仅用于前端获取登录session状态
    return 'loginVerify'

