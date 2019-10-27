#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/28'
# code is far away from bugs with the god
'''
import  time

class Point:
    def __init__(self):
        print("init")

    #一般用来做资源申请
    def __enter__(self):#这个除了self这个形参之外，其他形参没有意义，送不进去
        print('enter')

    #一般用来做资源清除
    def __exit__(self, exc_type, exc_val, exc_tb):
        #exc_type, exc_val, exc_tb这些都是关于异常的，只有有异常的时候才有用
        print('exc_val----->',exc_val)
        print('exc_type---->',exc_type)
        print('exc_tb------>',exc_tb)
        print('exit')
        return True#主要返回等效为True的，with里面的异常就会被压制


#上下文管理主要相关的魔术方法是__enter__和__exit__
#这两个方法是成对出现的
with Point() as f:
    print('--------------')
    time.sleep(2)
    print('!!!!!!!!!!!!!!!!!!!!!!!!')


pt = Point()
with pt  as f:#如果使用as语法，其值(即f)为enter的返回值，所以enter一般是self,但是不一定
    print('--------------')
    time.sleep(2)
    raise Exception("Your Error")
    print('!!!!!!!!!!!!!!!!!!!!!!!!')


#装饰器的实现
import datetime
from functools import wraps,update_wrapper


def timeit(fn):
    @wraps(fn)
    def wrapper(*arg,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*arg,**kwargs)
        end = datetime.datetime.now()
        print("{} token time is {}'s".format(fn.__name__,(end - start).total_seconds()))

        return ret

    return wrapper



@timeit
def add(x,y):
    '''
    :param x:
    :param y:
    :return:int
    '''
    time.sleep(2)
    return x + y

print(" 4 + 5 = {}".format(add(4,5)))



#上下文的实现
class TimeIt:
    def __init__(self,fn):
        self.fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()
        #return self#如果要使用as，那么这里一定要加返回值
        return  self.fn


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        total_time = (self.end - self.start).total_seconds()
        print("{} token {}'s".format(self.fn.__name__,total_time))



print("--------with语句实现--------------")

with TimeIt(add):
    print(add(4,5))

# print("--------with+as语句实现--------------")
# with TimeIt(add) as f:
#     print(f.fn(4,5))

print("--------with+as语句直接用（）调用--------------")
with TimeIt(add) as f:
    print(f(4,5))









#使用类装饰器
@TimeIt
def add(x,y):
    time.sleep(2)
    return x + y
