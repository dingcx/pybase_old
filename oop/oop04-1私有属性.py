#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/18'
# code is far away from bugs with the god
'''

class Person:
    _X = 11
    __y = 200#类变量也会被改名，_Person__y
    def __init__(self,name,age=18):
        # 私有变量，只是编程约定，不是语言特性，只要定义成了__attName,编译器就会将这个的名字改成_Class__attName,例如这里，__name变成了_Person__name
        self.__name = name
        self.__age = age
        #保护变量，只是编程约定，不是语言特性
        self._height = 69

    def getAge(self):
        return self.__age

    #私有方法，类里面使用，也会被改名_Person__getName
    def __getName(self):
        return self.__name


tom = Person('tom')
#Rprint(tom.name)
#print(tom.__age)
print(tom.getAge())

tom.__age = 100#动态增加实例属性__age
print(tom.__age)
print(tom.__dict__)#{'name': 'tom', '__age': 100, '_Person__age': 18, '_height': 69}
tom.__dict__['_Person__age'] = 100
print(tom.getAge())
tom._Person__age = 1000
print(tom.getAge())

print("Person.__dict__--->",Person.__dict__)



#属性装饰器
class Dog:
    def __init__(self,name,age,score=100):
        self._name = name
        self.__age = age
        self.__score = score



    @property  #getter，属性获取，Python要求必须有getter，才能有setter或者deleter,getter必须先有
    def age(self):
        return self.__age

    @age.setter#属性setter，这样就可以通过tom.age = 100来设置了
    def age(self,value):
        self.__age = value

    @age.deleter#del tom.age的时候会调用这个函数
    def age(self):
        del self.__age

    #这个几个的非装饰器版本
    def getscore(self):
        return self.__score

    def setscore(self,value):
        self.__score = value

    def delscore(self):
        del self.__score

    #property的__init__(self, fget=None, fset=None, fdel=None, doc=None)
    score = property(getscore,setscore,delscore)#提供getter函数


tom = Dog('tom',18)
print(tom._name,tom.age)

tom.age = 20
print(tom.__class__.__dict__)
print(tom.__dict__)


jerry = Dog('jerry',18)
print(jerry._name,jerry.age,jerry.score)

jerry.score = 10000
print(tom.__class__.__dict__)
print(tom.__dict__)


