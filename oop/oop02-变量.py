#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/18'
# code is far away from bugs with the god
'''


class Person:
    age = 3
    height = 170

    def __init__(self,name,age=18):
        self.name = name
        self.age = age


tom = Person('Tom')
Jerry = Person('Jerry',20)

print(Person.__class__)
print(str.__class__)
print(tom.__class__)
print('*'*40)

#类和对象的变化都可以通过__dict__来查看
print('类字典数据1：',Person.__dict__)

Person.age = 30
print('类字典数据2：',Person.__dict__)
print('tom对象字典1',tom.__dict__)
print('Jerry对象字典1：',Jerry.__dict__)
print(Person.age,tom.age,Jerry.age)
print(Person.height,tom.height,Jerry.height)

Jerry.height = 175#这个给实例对象增加了一个属性height,看实例的__dict__
print('类字典数据2：',Person.__dict__)
print('tom对象字典1',tom.__dict__)
print('Jerry对象字典1：',Jerry.__dict__)
print(Person.height,tom.height,Jerry.height)

print('-'*30)
tom.height += 10
print('类字典数据2：',Person.__dict__)
print('tom对象字典1',tom.__dict__)
print('Jerry对象字典1：',Jerry.__dict__)
print(Person.height,tom.height,Jerry.height)
#print(Jerry["height"])

print('-'*30)
Person.height += 10
print('类字典数据2：',Person.__dict__)
print('tom对象字典1',tom.__dict__)
print('Jerry对象字典1：',Jerry.__dict__)
print(Person.height,tom.height,Jerry.height)


print('-'*30)
Person.weight = 69
print('类字典数据2：',Person.__dict__)
print('tom对象字典1',tom.__dict__)
print('Jerry对象字典1：',Jerry.__dict__)
print(Person.weight,tom.weight,Jerry.weight)

#也可以通过字典的key来访问
print('-' * 30)
print(tom.__dict__['height'])
#如果是未定义的呢？报错还是为None,报错
#print(tom.__dict__['weight'])#KeyError: 'weight'


#Python实例对象属性的访问顺序是去__dict__里面查找的，顺序是：实例的__dict__,类的__dict__
#Python类对象只能访问类属性，也就是只能查找类的__dict__
class Animal():
    age = 12
    name = "Animal"
    x = "heihei"

    def __init__(self,name="dog",age=13):
        self.name = name
        self.age = age

    def showMyself(self):
        print("my name is {} and my age is {}".format(self.name,self.age))

dog = Animal()
cat = Animal("cat",19)
print("dog --> name is {} and age is {} and x is {}".format(dog.name,dog.age,dog.x))
print("cat --> name is {} and age is {} and x is {}".format(cat.name,cat.age,cat.x))
print("Animal --> name is {} and age is {} and x is {}".format(Animal.name,Animal.age,Animal.x))
