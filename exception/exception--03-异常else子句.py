#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/25'
# code is far away from bugs with the god
else子句：没有任何异常时发生
如果在函数内，try里面有return,或者finally里面有return，就不会执行
'''

try:
    ret = 1 * 0
    print(ret)
except ArithmeticError as e:
    print(e)
else:
    print('OK')
finally:
    print('fin')


print('------------------')


def foo():
    try:
        ret = 1 * 0
        return ret
    except ArithmeticError as e:
        print(e)
    else:
        print('OK')
    finally:
        print('fin')


foo()