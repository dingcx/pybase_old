#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/22'
# code is far away from bugs with the god
'''

#补丁，Monkey Patch在运行时，对属性、方法、函数等进行动态替换
#目的是为了通过替换、修改来增强、扩展原有代码的能力
#有一些第三方通过打补丁来增强标准库的功能

from oop043MonkeyPatch1 import Person
from oop043MonkeyPatch3 import get_score

def monkeypath4Person(cls):
    cls.get_score = get_score
    #cls = int  #这样把Person的类都变了


monkeypath4Person(Person)

tom = Person()
print(tom.get_score())



