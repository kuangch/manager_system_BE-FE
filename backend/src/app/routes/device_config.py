#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

# all api is for frontend interface
import json
from custom_libs.custom_decorator import check_login
from flask_application import app


@app.route('/config')
def config():
    return json.dumps({
        'code': 0,
        'data': {}
    })
