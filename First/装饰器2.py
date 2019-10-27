#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/3'
# code is far away from bugs with the god
一个更加通用的装饰器
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
def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def a(x,y,z):
    pass

def b(m,n,*,x,y,**kwargs):
    pass


#关于位置参数和key-word-only对要再次复习一下
#b(1,2,3,4,i=1)



def logger(fn,*args,**kwargs):#定义形参
    print("call function {}  x={},y={}".format(fn.__name__,*args))
    ret = fn(*args,**kwargs)#参数解构
    return ret


print('result = {}'.format(logger(add,4,5)))
print("result = {}".format(logger(sub,5,4)))


#柯里化上面的函数
def logger(fn):#定义形参
    def _inner(*args,**kwargs):
        print("call function {}  x={},y={}".format(fn.__name__,*args))
        ret = fn(*args,**kwargs)#参数解构
        return ret
    return _inner

print('result = {}'.format(logger(add)(4,5)))
