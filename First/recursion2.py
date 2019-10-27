#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/1'
递归recursion
    ①函数直接或者间接调用自身
    ②递归需要有边界条件，递归前进段、递归返回段
    ③递归一定要有边界条件
    ④当边界条件不满足的时候，递归前进
    ⑤当边界条件满足的时候，递归返回
用递归和循环来实现斐波拉契数列
'''


def fib_by_for(n):
    result = 0
    first = 1
    second = 0
    for i in range(n):
        result = first + second
        if n < 3:
            second = 1
        else:
            '''
            first = second
            second = result
            #使用交换的方式来实现
            '''
            first,second = second,result
        print(result)
    return second


print("last is {}".format(fib_by_for(8)))

print('使用递归实现fib----------------')
'''
使用递归来实现斐波拉契
'''
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib( n -2)


print(fib(8))

print("--------------------------")
def fib2(n):
    result = 0
    if n < 3:
        result = 1
    else:
        result = fib2(n - 1) + fib2( n -2)

    return result

print(fib2(8))


def fib3(n):
    return 1 if n < 3 else fib3( n -1) + fib3(n -2)



import sys
print(sys.getrecursionlimit())

import time
exec_before = time.time()
print(fib3(30))
exec_after = time.time()

print("执行时间为{}s".format(exec_after - exec_before))

def fib3(n,a=0,b=1):
    if n < 3:
        return a + b
    else:
        a,b = b,a+b
        return fib3(n-1,a,b)


exec_before = time.time()
print(fib3(600))
exec_after = time.time()

#这边的性能接近于单纯一个函数的时间
print("执行时间为{}s".format(exec_after - exec_before))


import datetime

time_now = datetime.datetime.now()
print(time_now.strftime('%f'))


