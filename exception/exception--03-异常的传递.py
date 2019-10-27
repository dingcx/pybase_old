#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/25'
# code is far away from bugs with the god
异常只要没有处理，就会不断向外抛出，直到被捕获，否则就会中断异常所在的线程
线程结束的状态是:1
'''


def foo1():
    return 1/0


def foo2():
    print('foo2 start')
    foo1()
    print('foo2 stop')


foo2()