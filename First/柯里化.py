#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/4'
# code is far away from bugs with the god
'''


def add(x):
    def _inc(y):
        #a =  x + y
        a = y
        return a
    return _inc

a =  add(3)(4)
print(a)