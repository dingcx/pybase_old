#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/10/5'
# code is far away from bugs with the god
'''


class A:
    def b(self):
        print("~~~~~~~~~b~~~~~")


    def __init__(self):
        self.b = 3000


    @classmethod
    def c(cls):
        print("~~~~~~~c~~~~~~~~~~~~~")

    @property
    def d(self):
        return 'abc'

a = A()
print(a.b)
#属性，类方法，和静态方法都可以被覆盖，但是property不能被覆盖
#a.d = 500

print(A.__dict__)
print(a.__dict__)

print("-----------描述器的应用---------------")

class StaticMethod:
    def __init__(self,fn):
        self.fn = fn

    #非数据描述器，所以只要实现__get__方法
    def __get__(self, instance, owner):
        print(self, instance, owner)
        return self.fn

    def __call__(self, *args, **kwargs):
        print("--------------------")
        self.fn(*args,**kwargs)


from functools import partial


class ClassMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        print(self, instance, owner)
        return partial(self.fn,owner)


class A:
    @StaticMethod  #这里相当于定义了foo = StaticMethod(foo),定义了这样的类属性，而StaticMethod是一个非数据描述器，所以最终foo这个变量名其实是去找__get__函数的返回值，所以__get__返回值要返回的是self.fn
    def foo():
        print("static method call")

    @ClassMethod
    def bar(cls):
        print("class method called")

a = A()
des = a.foo
des()


def func(x:int , y:str)->str:
    return str(x) + y


