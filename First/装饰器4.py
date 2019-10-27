#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/3'
# code is far away from bugs with the god

'''

import datetime

def logger(fn):
    def copy_properties(src,dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__

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
        return ret
    copy_properties(fn,wrapper)

    return wrapper


@logger
def add(x,y):
    '''this is add'''
    return x + x


add(4,5)
