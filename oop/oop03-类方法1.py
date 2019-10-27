#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/18'
# code is far away from bugs with the god
'''


def add_name(name='jerry'):#这只能叫装饰一个类，不能叫类装饰器
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper

@add_name('tom')
class Person:
    AGE = 10


#通过装饰器的方式来实现
#add_name(Person,'tom')
print(Person.__dict__["name"])

