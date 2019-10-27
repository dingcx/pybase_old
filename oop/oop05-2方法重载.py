#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/22'
# code is far away from bugs with the god
'''


class Dog:
    def __init__(self,name,age,score=100):
        self._name = name
        self.__age = age
        self.__score = score


'''
python天然支持重载
    1)类型不一致的时候，def add(x,y):不管x和y的类型，都能被函数add接收
    2）参数个数不同时，使用可变位置参数、关键字传参和默认值直接解决
'''





