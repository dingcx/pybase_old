#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/20'
# code is far away from bugs with the god
'''


def foo(bar=[]):
    bar.append('bar')
    return bar

foo()

'''
(['bar'],):print(foo.__defaults__)
{}:print(foo.__dict__)
None:print(foo.__kwdefaults__)
{'__new__': <built-in method __new__ of type object at 0x000000001D516260>, '__kwdefaults__': <attribute '__kwdefaults__' of 'function' objects>, '__qualname__': <attribute '__qualname__' of 'function' objects>, '__globals__': <member '__globals__' of 'function' objects>, '__module__': <member '__module__' of 'function' objects>, '__closure__': <member '__closure__' of 'function' objects>, '__annotations__': <attribute '__annotations__' of 'function' objects>, '__name__': <attribute '__name__' of 'function' objects>, '__repr__': <slot wrapper '__repr__' of 'function' objects>, '__code__': <attribute '__code__' of 'function' objects>, '__defaults__': <attribute '__defaults__' of 'function' objects>, '__call__': <slot wrapper '__call__' of 'function' objects>, '__get__': <slot wrapper '__get__' of 'function' objects>, '__dict__': <attribute '__dict__' of 'function' objects>, '__doc__': <member '__doc__' of 'function' objects>}

'''
print(foo.__defaults__)#默认参数
print(foo.__dict__)
print(foo.__kwdefaults__)#默认键值对
#print(foo.__class__.__dict__)
print(foo)

print('-' * 30)
for _ in range(3):
    tmp = foo()
    print(id(tmp),tmp)



print('-' * 40)


def foo(bar=None):
    if bar is None:
        bar = []
    bar.append('baz')
    return bar


for _ in range(3):
    tmp = foo()
    print(id(tmp),tmp)



print('-'*30)

def foo(a=[],*args,c=13,**kwargs):
    print(id(foo),foo.__defaults__)
    print(id(foo),foo.__kwdefaults__)


foo()
print(id(foo))


print('-'*30)


def foo(a=[],*args,c=3,**kwargs):
    print(id(foo),foo.__defaults__)
    print(id(foo),foo.__kwdefaults__)
    print('a',a)
    print('c',c)


foo(4,4)
print(id(foo))

#总结参数的顺序是：普通位置参数、缺省位置参数、可变位置参数(在*args之后的参数，一定是要用键值对来传参了)，keyword_only可以缺省，可变关键字参数
#
# 需要注意一点，函数在Python中也是一个对象，这个对象会当我们导入之后一直运行，默认参数会存储在这个对象的属性中__defaults__,
# 关键字参数会存储在__kwdefaults__中，当函数调用时，并且没有提供默认的参数值，就会从定义时赋值的地方取得值！
# 即使函数中给默认参数重新赋值了，下次调用还是会从定义赋值的地方取得值！










