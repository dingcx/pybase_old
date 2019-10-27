#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/26'
# code is far away from bugs with the god
这里主要实验容器类魔术方法
'''
class A(dict):
    def __missing__(self, key):
        print("Missing key :",key)
        return 0


a = A()
print(a[3])
print(a['4'])






