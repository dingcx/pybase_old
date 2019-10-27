#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/22'
# code is far away from bugs with the god
可以通过查看dir来查看函数、模块，作用域，类上都有什么
__dir__()这个魔术方法只对类有影响，具体什么区别可以试验下
'''
#dir()带参的话，收集的是该对象的变量，如果是无参的话，收集的是dir所在的作用域的变量
class A:pass


class B(A):pass


class C(B):
    def __dir__(self):
        return {'a':100}

print(C.__dict__)
print(dir(C))

print('-'*30)
c = C()
print(dir(c))


def a():
    #收集当前作用域的变量
    print(dir(),'-------------')

print(dir())
a()













