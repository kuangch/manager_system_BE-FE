#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2015 Dilusense Inc. All Rights Reserved.
from utils.my_constant import MyConstant


class GlobalInfo():
    """Global parameters class"""
    # db
    db_if_echo = False
    db_user = None
    db_pwd = None
    db_name_info_portal = None
    db_address = None
    db_port = None
    db_charset = None

    # logger
    logger_main = 'main'

    # flask
    flask_port = None

    # debug
    is_debug = False

    # path
    app_root_path = None
    log_path = None

    # serialized data save path
    persistent_data_path = None

    local_data_dir_name = None

    # 通过软连接结合python服务创建文件服务器
    rawdata_path = None
    rawdata_soft_link_path = '/static/rawdata'

    # 登录状态保持时间（默认5分钟）
    login_status_lifetime = MyConstant.web_config_login_status_lifetime_default




