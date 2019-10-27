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

这里主要实验类属性的时候
'''

class A:

    def __init__(self):
        print('A()-----------------')
        self.x = 100
    #定义了__get__,那么这个类就是描述器,如果只定义了__get__方法，就是非数据描述器，如果还实现了__set__或者__delete__，那么就是数据描述器
    def __get__(self, instance, owner):
        print("__get__'s self --->",self)#这里是A的实例
        print("__get__'s instance --->",instance)#我们发现如果是直接B.x来访问的话，instance为None，但是如果是B()来访问的话，是B的对象
        #在实例上加个属性呢？那么如果是类访问的话就有问题了，类访问的时候是None
        #instance.ins = 12
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


    def __delete__(self, instance):
        print("__delete__'s instance ----> ",instance)
        #del self.x,具体要怎么删除，可以在这里操作

    def __repr__(self):
        return "<A {}>".format(self.x)

class B:
    #类属性会在类对象生成的时候就执行，所以，当执行到这里的时候，A()的这个实力就会被创建了。
    x = A()#B.x如果在A中定义了__get__方法，那么就会触发__get__方法，并且将__get__方法的返回值赋值给x

    def __init__(self):
        print('B()----------')


a = A()
print("----B去调用了--------")
print(B.x.x)
print("----B调用完了--------")

print("----B开始实例化了--------")
b = B()
b.x
print("----B这段走完了--------")

print("----------开始实验set方法-------------")
#B.x = 1 #如果这边覆盖了，那么B这个类的x就没了，x属于类属性
b = B()
b.x = 2
print(b.__dict__)
print(B.__dict__)


print("---------------开始实验delete了--------------")
#del B.x#这样不会触发__delete__函数
del B().x
print(B.__dict__)