#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/29'
# code is far away from bugs with the god
反射相关的魔术方法：
    __getattr__,__setattr__(),__delattr__()
'''
class A:
    z = 100
    def __init__(self,x,y):
        self.x = x#如果有__setattr__方法，那么对对象赋值的时候就会触发__setattr__方法
        self.y = y
        self.__dict__['m'] = 5#但是这样赋值是不会触发__getattr__，__setattr__方法

    def __getattr__(self, item):
        print('__getattr__',item,type(item))
        #如果没有找到某个属性，不管是使用.的方式来查找还是使用getattr的方式来查找，都会触发这个函数，如果定义的话，没定义的话就会抛出异常
        #在这里，可以将没有找到的属性通过反射动态添加进来
        setattr(self.__class__,item,item)
        return getattr(self,item)

    def __setattr__(self, key, value):
        #
        print(key,'----->',value)
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('can not del attribute --->',item)

    def __getattribute__(self, item):
        print(item,'-------')
        return object.__getattribute__(self,item)#一般都是这么写的



print(A.z)
print('-'*30)

a = A(2,3)
print(a.x)
print(a.y)
print('-------------------')
print(a.z)
print(getattr(a,'x'))
print("----都没有触发__getattr__方法---")

print("------当没有找到属性的时候，会触发__getattr__函数-----")
print(a.b)
print(getattr(a,'b'))


print(a.__dict__)
print(A.__dict__)

#del a.__dict__['y']#这个是不会触发__delattr__
#del a.x#这个会触发__delattr__方法




