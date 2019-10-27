#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/9'
# code is far away from bugs with the god

'''
from functools import lru_cache
import time

@lru_cache()
def add(x=3,y=4):
    time.sleep(2)
    print(x)
    print(x + 1)
    return x + y
'''
输出结果：（lru_cache缓存的是函数的返回结果，所以一旦使用了这个函数，他只是假装执行了，其实使用的是系统中的缓存。）
3
4
1 7
2 7
3 7
缓存和缓冲是两个不同的概念
'''


print(1,add())
print(2,add())

print(3,add())



def testfn(x=2,y=3):
    print(x,y)


testfn(2)


#斐波拉契数列如果不用缓存，那么到了三十五的时候就已经非常慢了
@lru_cache() #速度非常快
def fib(n):
    if n < 3:
        return 1
    return fib(n -1 ) + fib(n - 2)

print(fib(35))
