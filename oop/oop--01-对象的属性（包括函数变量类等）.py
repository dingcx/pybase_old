#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   oop--01-对象的属性（包括函数变量类等）.py
@Time    :   2019/09/21 18:38:41
@Author  :   Ding ChangXiang 
@Version :   1.0
@Contact :   None
@License :   (C)Copyright 2018-2019
@Desc    :   None
'''

# here put the import lib
def add(x,y):
    return x + y


print("add.__name__--->",add.__name__)
print("add.__class__--->",add.__class__)
print("add.__class__.__name__--->",add.__class__.__name__)
print("type(add)---->",type(add))
print("type(add)---->",type(add).__name__)#这是一个字符串





class Person:
    age = 3
    def __init__(self,name="Jerry"):
        self.name = name
    
    def showname(self):
        print(self.name)

person = Person("tom")
print("person.__class__--->",person.__class__)
print("type(Person)---->",type(person)) 
  
print("Person.__class__--->",Person.__class__)
print("type(Person)---->",type(Person))   


