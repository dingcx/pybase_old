#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/19'
# code is far away from bugs with the god
'''


class Document:
    def __init__(self,content):
        self.content = content

    def print(self):#这个就可以认为是抽象方法
        raise NotImplementedError


#假设是第三方提供的类
class Word(Document):pass


#假设是第三方提供的类
class Pdf(Document):pass


#假设我们要自己增强第三方的库，OCP原则，多继承，少修改
class PrintableWord(Word):
    def print(self):
        print('Word:',self.content)


class PrintablePdf(Pdf):
    def print(self):
        print('pdf:',self.content)


pw = PrintableWord('test word')
pw.print()

p = PrintablePdf('test pdf')
p.print()



#使用装饰器来给类注入未实现的方法
def printable(cls):
    # 这里的self无非就是和print(self)这个类方法保持一致而已
    def _print(self):
        print('{}:{}'.format(type(self).__name__,self.content))

    cls.print = _print
    return cls


@printable
#1)等价 PrintablePdf = printable(PrintablePdf),
#2)printable要返回什么，要看printable(PrintablePdf)的返回值要怎么使用
class PrintablePdf(Pdf):pass



p = PrintablePdf('test pdf')
p.print()



#Mixin
class PrintableMixin:
    def print(self):
        print('{}:{}'.format(type(self).__name__,self.content))


class PrintableWord(Word,PrintableMixin):pass

#Python中很重要的一个方法就是类的mro()，这个可以看出类的查找方法顺序
pw = PrintableWord('test word')
#pw.print()
print(pw.__class__.mro())



print('-'*30)




#Mixin是利用Python的多继承来实现的,Mixin比装饰器好的，就是Mixin可以被继承，缺什么补什么
class PrintableMixin:
    def print(self):
        print('{}:{}'.format(type(self).__name__,self.content))


class PrintableWord(PrintableMixin,Word):pass#混进谁，就是优先用谁的，要多去查看不同情况下的mro


pw = PrintableWord('test word')
pw.print()
print(pw.__class__.mro())


#查看Mixin被继承之后的mro
class PrintableWordEx(PrintableWord):
    def print(self):
        print('-'*40)
        print('{}:{}'.format(type(self).__name__, self.content))
        print('-' * 40)


f = PrintableWordEx('Ex')
f.print()
print(f.__class__.mro())

import math


class Shape:

    def __init__(self,**edges):pass

    def area(self):
        raise NotImplementedError


class Triangle(Shape):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a)*(p-self.b)*(p-self.c))


#测试
triangle = Triangle(3,4,5)
print('triangle\'area is ' + str(triangle.area()))
#print(triangle.area())

class Rectangle(Shape):

    def __init__(self,weight,height):
        self.weight = weight
        self.height = height

    def area(self):
        return self.weight * self.height


#测试
rectangle = Rectangle(3,4)
print('rectangle\'area is ' + str(rectangle.area()))


class Circle(Shape):

    def __init__(self,redius):
        self.redius = redius

    #也可以使用属性装饰器
    @property
    def area(self):
        return math.pi * self.redius * self.redius


#测试
circle = Circle(3)
print('circle\'s area is ' + str(circle.area))


import json


class SerializableMixin:
    def seriablize(self,t='json'):
        if t.lower() == 'json':
            return json.dumps(self.__dict__)
        elif t.lower() == 'msgpack':
            #因为缺少msgpack的库，暂时未实现
            raise NotImplementedError('msgpack don\'t implement')
        else:
            raise NotImplementedError('only implement json and msgpack')

#将圆形的字典来序列化
class Circle(Shape):

    def __init__(self,redius):
        self.redius = redius

    #也可以使用属性装饰器
    @property
    def area(self):
        return math.pi * self.redius * self.redius


class SerializableCircleMixin(SerializableMixin,Circle):pass


scm = SerializableCircleMixin(4)
print(scm.area)
print(scm.seriablize('Json'))
#print(scm.seriablize('msgpack'))





