#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/28'
# code is far away from bugs with the god
'''
from contextlib import contextmanager

#这是一个用函数实现的上下文管理的装饰器
@contextmanager
def foo():
    print('enter')#yield之前相当于__enter__函数
    yield  #yield 5，yield的值只能有一个，作为__enter__方法的返回值
    print('exit')#yield之后相当于__exit__函数


with foo() as f:#f接收yield语句的返回值
    print(f)


#这样的写法是为了给函数增加一种上下文管理的机制

