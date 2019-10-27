#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/24'
# code is far away from bugs with the god

'''

class Point:

    z = 6

    def __init__(self,x,y):
        self.x = x
        self.y = y


p1 = Point(4,5)
print(p1.x)


print(getattr(p1,'x'))

for n in dir(p1):
    print(type(n),n)
    print(getattr(p1,n))


if hasattr(p1,'y'):
    print(getattr(p1,'y'))#等价于p1.y

setattr(p1,'b',100)#等价于p1.b = 100

print(getattr(p1,'__dict__'))


setattr(Point,'show',lambda  self:print(self.x,self.y))
print(Point.__dict__)
p1.show()
getattr(p1,'show')()


setattr(p1,'show1',lambda self:print(self,'_____________'))

print(p1.__dict__)
print(Point.__dict__)
#p1.show1()
p1.show1(p1)


