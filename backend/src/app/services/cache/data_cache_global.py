#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import datetime


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class DataCacheGlobal(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.cache = {}

    def __contains__(self, key):
        return key in self.cache

    def update(self, key, value):
        self.cache[key] = {}
        self.cache[key]['time'] = datetime.datetime.now()
        self.cache[key]['value'] = value

    def get(self, key):
        if key in self.cache:
            return self.cache[key]['value']
        else:
            return None

    def get_data_cached_time(self, key):
        if key in self.cache:
            return self.cache[key]['time']
        else:
            return None