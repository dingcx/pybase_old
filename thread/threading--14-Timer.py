#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/12'
# code is far away from bugs with the god
'''

from threading import Timer,Thread


def add(x,y):
    print(x + y)



t = Timer(5,add,(4,5))

#在start之前cancel和start之后的区别
t.cancel()
t.start()


print("===========")


