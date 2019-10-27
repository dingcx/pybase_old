#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/3'
# code is far away from bugs with the god

'''

import datetime


def copy_properties(src):
    def _copy(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        #return dest
        #如果没有返回值，那么就相当于返回None，最终copy_properties(src)(dest)返回的就是None
    return _copy


def logger(fn):
    @copy_properties(fn)
    #这里等价于 wrapper = copy_properties(fn)(wrapper),返回wrapper，然后再进行执行wrapper，所以如果返回的是None的话，就不能被调用了
    def wrapper(*args,**kwargs):
        '''this is wrapper function'''
        print("可以在这里做一些操作")
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now() -start).total_seconds()
        print("Function {} took {}s".format(fn.__name__,delta))

        if delta > 5:
            print("so low")
        else:
            print("so fast")

        print("这里可以做一些后续操作")
        return ret #这边返回的是fn的执行结果
    #copy_properties(fn,wrapper)
    #柯里化：copy_properties(fn)(wrapper)，fn和wrapper无非也是一个对象而已

    return wrapper


@logger  # 用logger(add)  =>  add
def add(x,y):
    '''this is add'''
    return x + y


add(4,5)
