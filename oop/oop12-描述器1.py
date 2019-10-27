#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/25'
# code is far away from bugs with the god
描述器用到了三个魔术方法：
    __get__(),__set__(),__delete__()
'''

'''
描述器的表现

这里主要实验对象属性的时候

主要要注意的是，数据描述器和非数据描述器之间属性的访问顺序
'''

class A:

    def __init__(self):
        print('A()-----------------')
        self.x = 100

    def __get__(self, instance, owner):
        print("__get__'s self --->",self)#这里是A的实例
        print("__get__'s instance --->",instance)#我们发现如果是直接B.x来访问的话，instance为None，但是如果是B()来访问的话，是B的对象
        print("__get__'s owner --->",owner)#这里是B的类
        #在owner上加一个类属性上去,加上去了
        owner.at = "dingcx"
        print('~~~~~~~~~~')
        return self

    def __set__(self, instance, value):
        print('~~~~~__set__~~~~~')
        print("__set__'s self --->",self)#A的实例
        print("__set__'s instance --->",instance)#B的实例
        print("__set__'s value --->",value)#设置的属性的值
        #instance = value
        instance.z = value#这样将value的值给进了b里面
        #instance.x = value
        instance.__dict__['x'] = value#这是存放在dict里面的，所以一样遵循，数据描述器的优先级高于dict的原则


    def __delete__(self, instance):
        print("__delete__'s instance ----> ",instance)


    def __repr__(self):
        return "<A {}>".format(self.x)

class B:
    #类属性会在类对象生成的时候就执行，所以，当执行到这里的时候，A()的这个实力就会被创建了。
    x = A()#B.x如果在A中定义了__get__方法，那么就会触发__get__方法，并且将__get__方法的返回值赋值给x

    def __init__(self):
        print('B()----------')
        self.x = 10#当对象属性和类属性同名时，虽然是对象的属性，但是触发了类属性的赋值



class C:
    x = "dingcx"
    def __init__(self):
        self.x = 100


b = B()
print(b.x)
print("B.__dict__---> ",B.__dict__)
print("实例的dict里面有x吗？")
print("b.__dict__---->",b.__dict__)


print("实验有描述器和没定义描述器的区别")
c = C()
print(c.__dict__)#类的dict里面是"dingcx",实例的dict里面是100
print(C.__dict__)

