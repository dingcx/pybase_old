#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/18'
# code is far away from bugs with the god
'''

class Person:

    def __init__(self,name="tom"):
        self.name = name

    #这种定义是可以的，但是最好不用，也会在类字典中
    def normal_function():
        print('normal')

    @classmethod #这是一个装饰器,用来使方法与类相关
    def class_method(cls):
        print('class method--->',cls,hex(id(cls)),hex(id(Person)))

    @classmethod #
    def class_method2(self):#不管方法的形参是cls还是self，只要用classmethod修饰，都是与类绑定
        print('class method,when arg is self--->',self,hex(id(self)),hex(id(Person)))

    def method(self):
        print("method self's name is {}".format(self.name))

    @staticmethod
    def static_method():
        print("static method")

    @staticmethod
    def static_method2(cls):#这个cls是什么？
        print("static method cls-->",cls)

Person.normal_function()
#Person().normal_function()#该方法没有和实例绑定，所以当我们调用的时候，就会报错了

#对于实例方法来说，method方法与Person类的实例绑定了，
#Person.method()报错，method的参数少了一个self实参
#Person.method("123")#这样没问题，但是如果method方法中有对self属性的操作，那就出问题了

Person().method()

Person().class_method()
Person.class_method()
Person().class_method2()
Person.class_method2()
print(Person.__dict__)
print(Person().__dict__)


#类方法和实例方法会将class和实例作为第一参数传入，但是静态方法是不会的
#类操作类的属性，实例方法操作实例的属性，静态方法对类和实例都没啥影响，就和普通函数一样，只不过是加了一个命名空间罢了
Person.static_method()
Person().static_method()














