#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god
Python中：
    所有非object类都继承自object类
    所有类的类型包括type类都是type
    type类继承自object类，object类的类型也是type类

'''


class A:
    pass


class B(A):
    pass

#type也是一个类
print(type(A))
print(type(B))

#即便我们使用class关键字来创建一个类，最终也是使用一样的方法
XClass = type('X',(),{})

print(type(XClass))
print(XClass)
print(XClass.mro())


XClass = type('X',(object,),{'x':100})#等价于class构造器，字典是类属性
print(type(XClass))
print(XClass)
print(XClass.mro())
print(XClass.__dict__)
print(XClass().__dict__)

print('-' * 40)


def __init__(self):
    self.y = 2000


def show(self):
    print(self.y)


XClass = type('X',(object,),{'x':100,'show':show,'__init__':__init__})
#XClass = type('X',(object,),{'x':100,'show':show,'y':2000})#等价于class构造器，字典是类属性
print(XClass.__dict__)
print(XClass().__dict__)
XClass.show(XClass())
XClass().show()












