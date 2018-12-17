#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2018 Dilusense Inc. All Rights Reserved.


"""=======================================

    company : Dilusense
     author : Kuangch
       date : 2018/7/31

======================================="""

import time

class DataCache():

    def __init__(self):
        self.cache = {}

    def __contains__(self, key):
        return key in self.cache

    def update(self, key, value):
        self.cache[key] = {}
        self.cache[key]['time'] = time.time()
        self.cache[key]['value'] = value

    def get(self, key):
        if key in self.cache:
            return self.cache[key]['value']
        else:
            return None

    def is_obsolete(self,key,duration=3):
        if key in self.cache:
            return abs(time.time() - self.cache[key]['time']) > duration
        else:
            return True