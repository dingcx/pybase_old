#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/29'
# code is far away from bugs with the god
'''


def foo():
    try:
        1/0#这个异常在后面是不会被捕获的
        f = open('test1.txt')
        print(f)
    except FileNotFoundError as e:
        print('{} {}'.format(e.__class__,e.errno,e.strerror))
    finally:
        print('清理工作')
        return


#此时调用不会抛出异常，相当于异常被压制了，所以在finally中很少return
foo()
