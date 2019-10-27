#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/25'
# code is far away from bugs with the god
捕获异常：
    try ... except:
程序会在try中去检查异常，如果发生异常将其捕获
    1)在异常发生的地方会转到except语句执行
    2)如果不发生异常，则直接往下走，try对应的except语句将被跳过
    3）如果异常发生，但是exception中找不到对应的except的父类或者本身的异常，就会将该异常抛出给程序

异常捕获规则：
    捕获是从上到下一次比较，如果匹配，则执行匹配的except语句块（匹配到异常类的父类或者自己）
    如果被一个except语句捕获，其他except语句就不会再次捕获了
    如果没有任何一个except语句捕获到这个异常，就会将该异常向外抛出

捕获的原则：从小到大，从具体到宽泛（这个是告诉我们写代码的时候，应该这么做）


常见的内建异常类
    1）BaseException是所有内建异常类的基类
    2）SystemExit,sys.exit()函数引发的异常
    3）KeyboardInterrupt:键盘中断，捕获用户中断行为，Ctrl+C
    4）ArithmeticError所有算数计算引发的异常，

'''


#SystemExit异常演示
import sys

try:
    #try中测试三种情况
    # print('hello')
    # sys.exit(1)
    sys.exit(0)
# except SystemExit:
#     print('sysExit')
except BaseException:
    print('out')
print('Outer')


class ChildIndexError(IndexError):
    pass


lst = []

try:
    #这边真正抛出的异常是IndexError
    print(lst[2])
# except Exception:#如果是祖先异常类，可以捕获这个异常
#     print('Exception')
# except LookupError:#父类也是可以捕获的
#     print('LookupError')
except ChildIndexError:#但是如果是子类的话，就不会捕获
    print('KeyError')
except LookupError:
    print('放在子类后面也是可以捕获的')

#KeyboardInterrupt演示，这个要在Terminal中演示
try:
    import time
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Ctrl + c')



