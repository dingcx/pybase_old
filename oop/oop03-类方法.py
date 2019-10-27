#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/18'
# code is far away from bugs with the god
'''
class Person:
    AGE = 10


def add_name(cls,name):
    cls.NAME = name

add_name(Person,'tom')
print(Person.__dict__["NAME"])#实现了


