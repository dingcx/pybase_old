#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/22'
# code is far away from bugs with the god
魔术方法：


'''


class A:pass


class B(A):pass


class C(B):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        #return cls()#这里为什么不能用cls()呢？因为cls()就会调用一次__init__方法，所以这里就会发生死循环了
        return super().__new__(cls)#调用super()的__new__方法，会通过mro一直往上走，直到找到实现了该方法的类。

    def __init__(self,name):
        #super().__init__()
        self.name = name

#__hash__()：

c = C('Tom')
print(c.__dict__)
print(dir(c))


#设计一个类，要有equel方法和hash方法

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x,self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1,2)
p2 = Point(1,2)
print("p1和p2是否实现了去重",{p1,p2})


#bool
class A:pass


if A:
    print(1,'True')


if A():
    print(2,'True')

#这也是为什么int =1 的时候可以等效为TRUE
print(bool(A),bool(A()))#没有__bool__的话，默认为真

class B:
    def __bool__(self):
        return False

if B:
    print("B1",'True')


if B():
    print("B2",'True')

#如果提供了__bool__()函数，那么在使用bool()转换的时候，会根据该函数的返回值来转换
#如果没有提供__bool__函数，那么会根据__len__()函数是否为0来判断其容器的大小
class C:
    def __len__(self):#只能返回大于等于0的整数
        #return 1.1
        #return 0-1
        return 0

    def __bool__(self):
        return True

print("len和bool都提供的情况下,使用__boo__来转换：" ,bool(C),bool(C()))


#表述对象自身（可视化），也就是使用字符串来表达一个对象
# str:直接转换成字符串的时候调用这个方法
# repr：间接引用打印的时候使用这个方法，
# 如果str没有提供，那么会所有的都会去找repr,如果repr没有提供，那么直接打印就找str，间接引用打印就找父类的repr。
# __bytes__：在使用bytes(对象)时，表述对象的形式，该函数只能返回bytes对象

class F:

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'repr name = {}'.format(self.name)

    def __str__(self):
        return 'str name = {}'.format(self.name)

    def __bytes__(self):
        #return 'F'.encode()
        import json
        return json.dumps(self.__dict__).encode()


f = F('Tom')
print("f---->",f)#强制类型转换，使用__str__函数
print("f---->{}".format(f))#format默认也是使用__str__函数
print(repr(f),"---->",str(f))#使用str来构造也是使用__str__(),repr函数使用的是__repr__()函数
print(repr("f---->{}".format(f)))

print([f,f])#如果是在集合中，或者说是其他对象中引用的该实例，就是使用__repr__函数来tostring了。
print((f,f))
print({f,f})
print('{}'.format({f,f}))
print('{}'.format(*{f,f}))#这里使用了解构，所以就使用了第一个实参，然后用format施加到f上，所以使用的是str

print(bytes(f))

b = f.__class__(f.name)#一个__class__返回的也是一个可调用对象
print(b)

