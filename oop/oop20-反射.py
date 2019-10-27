#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/28'
# code is far away from bugs with the god
反射也就是说，能够通过一个对象，找出其type，class、method和attribute的能力
具有反射能力的函数：type(),isinstance(),callable(),dir(),getattr()

'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)

p1 = Point(3,4)

for n in dir(p1):
    print(type(n),n)
    print(getattr(p1,n))


print("------循环外面--------------")
print(getattr(p1,'x'))
print(getattr(p1,'show'))

print(getattr(p1,'__dict__'))
print(getattr(Point,'__dict__'))

setattr(Point,'getxy',lambda self:print(self.x,self.y))
p1.getxy()
print(getattr(p1,'__dict__'))
print(getattr(Point,'__dict__'))

getattr(p1,'getxy')()

setattr(p1,"show2",lambda self:print(self,'-----------------'))#这样没有绑定实例
print(getattr(p1,'show2'))

#p1.show2()
getattr(p1,'show2')(p1)

print(hasattr(p1,'show2'))












