#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/3'
# code is far away from bugs with the god
装饰器的实现
'''

def logger(fn):#定义形参
    '''
    文档字符串的使用,必须在函数的一行
    :param fn:
    :return: ret fffff
    '''
    def wrapper(*args,**kwargs):
        print("call function {}  x={},y={}".format(fn.__name__,*args))
        ret = fn(*args,**kwargs)#参数解构
        return ret
    return wrapper

'''
讲述文档字符串的使用
'''
@logger #这边等价于 add = logger(add) ==> 并且返回add 就是wrapper
def add(x,y):
    return x + y

print(logger.__doc__)


print('result = {}'.format(logger(add)(4,5)))

ret = add(4,5)
print(ret)


