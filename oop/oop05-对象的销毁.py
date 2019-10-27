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

    def __del__(self):
        print("------del--，主要是为了做一些清理工作，比如说文件关闭，网络关闭--------")



#对象的销毁
tom = Dog('tom',18)
tom1 = tom
tom2 = tom1
jerry = Dog('jerry',18)

print("--------对象开始销毁-----------------")
del tom1
del tom
del tom2
print("--------对象结束销毁-----------------")

'''
--------对象开始销毁-----------------
------del----------#只销毁一次，只有引用计数器为0的时候才会被销毁
--------对象结束销毁-----------------
------del----------#Jerry开始销毁了
'''
