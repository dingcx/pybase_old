#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/28'
# code is far away from bugs with the god
'''
import time
import datetime
from functools import wraps,update_wrapper


print("--------使用类装饰器--------------")
class TimeIt:

    def __init__(self,fn):
        self.__fn = fn
        #类的文档可以在__init__文档中来更新,两种方法都可以使用
        #update_wrapper(self,fn)
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.start = datetime.datetime.now()
        ret = self.__fn(*args,**kwargs)
        self.end = datetime.datetime.now()
        total_time = (self.end - self.start).total_seconds()
        print("{} token {}'s".format(self.__fn.__name__,total_time))

        return ret


def timeit(fn):
    @wraps(fn)
    def wrapper(*arg,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*arg,**kwargs)
        end = datetime.datetime.now()
        print("{} token time is {}'s".format(fn.__name__,(end - start).total_seconds()))

        return ret

    return wrapper



#类装饰器是使用了可调用对象,如果是两个装饰器呢？有两个装饰器的话，执行顺序是从下往上执行的
@TimeIt
#@timeit
def add(x,y):
    '''
    :param x:
    :param y:
    :return: int
    '''
    time.sleep(1)
    return x + y


print(add(4,5))

#其实是否是可调用对象，只要看是否可以标志符+（）TimeIt()没问题，所以这也是一个可调用对象
print(callable(TimeIt))
print(callable(TimeIt(add)))
print(type(TimeIt(add)))
print("add.__doc__--->",add.__doc__)

