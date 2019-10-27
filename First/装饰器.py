#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/3'
# code is far away from bugs with the god
装饰器的使用
'''

def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def logger(fn,x,y):
    print("call function {}  x={},y={}".format(fn.__name__,x,y))
    ret = fn(x,y)
    return ret


print('result = {}'.format(logger(add,4,5)))
print("result = {}".format(logger(sub,5,4)))
