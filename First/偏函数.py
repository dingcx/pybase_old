#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/8'
# code is far away from bugs with the god
#偏函数的使用，之后再把functools模块熟悉下
'''
from functools import partial
import inspect

def add(x,y):
    return x + y


#add(4,5)
newadd1 = partial(add,4)
print(newadd1(5))


#add(4,5)
newadd2 = partial(add,y=5)
print(newadd2(4))















