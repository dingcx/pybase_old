#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/17'
# code is far away from bugs with the god
类对象：类的定义就会生成一个类对象
类的属性：类定义中的变量和类中定义的方法都是类属性
类变量：MyClass.x就是类MyClass的变量
'''
class MyClass:
    """A example class"""
    x = 'abd'  #类属性

    def foo(self):#类属性foo，也是方法，方法是属于类的，类属性也属于类的，self.age  = 20属于实例的
#实例变量是每一个实例自己的变量，是自己独有的，类变量是类的变量，是类的所有的实例共享的属性和方法（包括类自己本身也可以使用。）
        return "My class"

print("MyClass--->",MyClass)
print("MyClass.x--->",MyClass.x)
print("MyClass.foo--->",MyClass.foo)
print("MyClass.__doc__--->",MyClass.__doc__)


#实例化，每次实例化都会调用类的__init__方法，构造器，这个方法的第一个参数必须给self,这个self是__new__方法实例化出来的对象，送到了__init__方法做实参，在__init__方法中做的其他操作，都是对这个对象进行一系列的操作，__init__()要求必须返回None
a = MyClass()
a.foo()
MyClass.foo(a)
print("a.x------>",a.x)#对象也可以访问类的属性

print('类字典：',a.__dict__)
print('类字典：',MyClass.__dict__)

class MyClass2:
    def __init__(self):
        print('init')
        self.age  = 20



print(MyClass2)
print(MyClass2())





