#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/29'
# code is far away from bugs with the god

'''

class A:
    X = 1

    #只要是一个可迭代对象就可以了
    #__slots__ = 'y z'.split()#如果这里面定义的属性，才能被定义到对象的属性中
    #__slots__ = ['y', 'z', 'z','X']
    __slots__ = ['y','z','z']

    def __init__(self):
        self.y = 5
        self.z = 6
        #这里也是一样的，如果__slots__中没有定义对应的属性，不管是在类里面用self来添加还是在外部添加都不行
        #self.a = 4


print(A.__dict__)
a = A()

#只要定义了__slots__，对象的dictionary就没有了，为什么要定义__slots__,因为字典是很耗空间的，所以采用一个更加简单的方式，来存储对象的属性会更加合理，我们也可以看到，__slots__对类属性来说是没有影响的
#print(a.__dict__)

print(a.X)
print(a.y)
print(a.z)
#a.X = 1000


#这里也是一样的，如果__slots__中没有定义对应的属性，不管是在类里面用self来添加还是在外部添加都不行
#a.a = 1

class M:
    X = 10

    def __init__(self):
        self.x = 12


m = M()
print(m.X)
m.X = 12
print(m.X)

#我们发现一旦定义了__slots__，那么，类属性X就变成了只读的了，如果将X给了__slots__呢？不行，会报与类变量（属性）冲突的错误
#并且只会影响当前实例的字典
#父类的__slots__不会影响子类
#__slots__使用场景：使用需要构建在数百万以上的对象，且内存容量较为紧张，实例的属性简单、固定且不用动态增加的场景


#题外话，分析两个问题
print(type(None))#None是一个值，单值，是NoneType的实例
print(type(NotImplemented))#NotImplemented是一个值，单值，是NotImplementedType的实例
print(type(NotImplementedError))#NotImplementedError是一个类型


def foo():
    raise NotImplemented

#foo()