#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/6'
# code is far away from bugs with the god

'''
def add(x:int,y:int) -> int:
    return x + y

print(add(3,4))
#不会做编译时的强制限制
print(add('xyma','dddd'))


print(add.__annotations__)


import inspect
@property
inspect.isclass(add)




