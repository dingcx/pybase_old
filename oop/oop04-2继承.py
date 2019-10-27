#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/19'
# code is far away from bugs with the god
'''

class Animal:
    def __init__(self):
        self.a1 = 'a1'
        self.__a2  = 'a2'
        print('A init')

    def shout(self):
        print('{} shouts'.format(type(self).__name__))


class Cat(Animal):
    pass

cat = Cat()
print(cat.__dict__)


'''
几个重要的特殊属性：
    __base__:只有类才有，父类
    __bases__:父类们
    __mro__:查看类的继承树,方法的查找顺序
    mro():一样的
    __subclasses()__:
    
'''
print(int.__subclasses__())
print(True + True)

#继承中的访问控制，这个例子要从课件里面去看


#这里自己再附加一个疑问
class Father():
    def __init__(self):
        self.__i = 100

    def geti(self):
        return self.__i

class Child(Father):
    pass

child = Child()
print("child.geti()--->",child.geti())
print("type(child.geti)--->",type(child.geti))


#属性、方法的查找顺序（单纯从单继承来看）


#方法重写override--->方法的查找顺序


#继承的__init__方法
class ForInitF():
    def __init__(self):
        self.a1 = 'a1'
        self.__a2 = 'a2'
        print('A init')


class ForInitB(ForInitF):
    def __init__(self):
        super(ForInitB,self).__init__()#如果不调用父类的初始化方法，会覆盖父类的__init__方法

