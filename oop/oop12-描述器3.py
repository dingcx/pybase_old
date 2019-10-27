#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/10/5'
# code is far away from bugs with the god
'''


class Person:
    def __init__(self,name:str,age:int):
        params = ((name,str),(age,int))
        if not self.checkdata(params):
            raise TypeError
        print("OK")
        self.name = name
        self.age = age

    def checkdata(self,params):
        for k,v in params:
            if not isinstance(k,v):
                return False
        return True


p1 = Person("dingcx",12)
#p2 = Person("dingcx",'12')


#如果使用描述器来实现呢？
class TyepCheck:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is not None:
        #if not isinstance(instance,None):
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value,self.type):
            raise TypeError
        instance.__dict__[self.name] = value


class Human:
    name = TyepCheck('name',str)
    age = TyepCheck('age',int)

    def __init__(self,name:str,age:int):

        self.name = name
        self.age = age


h = Human('dingcx',12)
print("h's __dict___ --->",h.__dict__)
print(h.name,h.age)




d = None
print(isinstance(d,type(None)))#为什么None不是一个类型呢？


