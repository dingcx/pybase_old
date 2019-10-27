#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/3'
# code is far away from bugs with the god
enumerate的使用
'''

lst = [2,1,23,4,5,43,2,3,4,2,1]

a = enumerate(lst)
print(type(a))
for i,x in a:
    #print(next(a))
    print(i,x)


def add(x,y):
    return x + y

print(add(4,5))


def add(x):
    def fn(y):
        return x + y

    return fn


print(add(4)(5))