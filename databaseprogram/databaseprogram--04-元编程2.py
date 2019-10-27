#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god
Python中：
    所有非object类都继承自object类
    所有类的类型包括type类都是type
    type类继承自object类，object类的类型也是type类
'''


class ModelMeta(type):#一旦继承自type，那么我们就称为元类，元类是可以用来构造其他类的类
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        return super().__new__(cls,*args,**kwargs)


class A(metaclass=ModelMeta):
    pass


print('-' * 40)



class ModelMeta(type):#一旦继承自type，那么我们就称为元类，元类是可以用来构造其他类的类
    def __new__(cls, name,bases,attrs ):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        return super().__new__(cls,name,bases,attrs)


class A(metaclass=ModelMeta):
    id = 100

    def __init__(self):
        self.x = 2000


print('type(A) is ',type(A))


print('~' * 40)
class B(A): #继承
    id = 'b'


print('~' * 40)
print('B.mro() is ',B.mro())

print('~' * 40)

C = ModelMeta('CClass',(),{'y':2000})
print('type(C) is ',type(C))


class D(ModelMeta): #这也是走继承的线
    pass


print('type(D) is ',type(D))








