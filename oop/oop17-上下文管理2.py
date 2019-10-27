#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/28'
# code is far away from bugs with the god
'''
import time
import datetime

print("--------enter返回self，依然要用f(4,5)怎么实现？提示：使用__call__()函数--------------")
class TimeIt:
    def __init__(self,fn):
        self.__fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()
        return  self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        total_time = (self.end - self.start).total_seconds()
        print("{} token {}'s".format(self.__fn.__name__,total_time))

    def __call__(self, *args, **kwargs):
        print("__call__")
        ret = self.__fn(*args,**kwargs)
        return ret

def add(x,y):
    time.sleep(1)
    return x + y

with TimeIt(add) as f:
    print(f(4,5))