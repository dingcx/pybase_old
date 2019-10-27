#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/12'
# code is far away from bugs with the god
'''

#3.4版本之前的
from os import path

p = path.join('F:/profiles/JetBrains/PycharmProjects/file','sysconfig','network')

#p是str
print(type(p),p)

print('split函数,',path.split(p))
print('当前路径：',path.abspath('.'))

#两个重要的函数，dirname()和basename()，其实最好就是去看看path这个类


p1 = path.abspath(__file__)

print(p1,path.basename(p1))
#F:\profiles\JetBrains\PycharmProjects\file
while p1 != path.dirname(p1):
    p1 = path.dirname(p1)
    print(p1,path.basename(p1))

p = 'F:/'
#也就是说，最后的dirname就不会继续往下分割了。
print(p == path.dirname(p))



#3.4版本之后，可以使用pathlib模块
from pathlib import Path

p = Path()
print(type(p),p,p.absolute())

p = Path('a/b/c')
print(p,type(p),p.absolute())

p = Path('/etc','sysconfig','network')
print(p,type(p),p.absolute())

#Path将/操作符重写了，可以直接使用/来拼接路径，左右都可以拼接
p = p / 'a'
print(p,type(p),p.absolute())

print('------------------------------------')
p = 'a' / p
print(p,type(p),p.absolute())



