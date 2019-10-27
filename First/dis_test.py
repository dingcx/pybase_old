#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/1'
# code is far away from bugs with the god
#dis模块的使用
#   dis模块主要是用分析字节码的一个内置模块，经常用得方法是dis.dis([bytesource])
#这个程序主要是为了通过查看字节码，来分析Python交换的本质
    Python的变量并不直接存储值，而只是引用一个内存地址，交换变量时，只是交换了引用的地址
'''

import dis


def func(a,b):
    a,b = b,a
    print(a,b)

a,b = 10,11
func(a,b)

dis.dis(func)
'''
这段的输出
 17           0 LOAD_FAST                1 (b)
              3 LOAD_FAST                0 (a)
              6 ROT_TWO
              7 STORE_FAST               0 (a)
             10 STORE_FAST               1 (b)

 18          13 LOAD_GLOBAL              0 (print)
             16 LOAD_FAST                0 (a)
             19 LOAD_FAST                1 (b)
             22 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             25 POP_TOP
             26 LOAD_CONST               0 (None)
             29 RETURN_VALUE

'''


