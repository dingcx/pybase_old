#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/2'
# code is far away from bugs with the god
使用递归求阶乘
'''

#使用循环实现阶乘

def factorial_by_for(n):
    result = 1
    for i in range(n+1):
        if i < 2 :
            pass
        else:
            result *= i
    return  result


print(factorial_by_for(10))


def factorial_by_recursion(n):
    if n < 2:
        return 1
    else:
        return n * factorial_by_recursion(n-1)


print(factorial_by_recursion(10))


def fac(n,facvar=1):
    if n == 1:
        return facvar
    facvar = facvar * n
    return fac(n-1,facvar)

print("--------------------------")


#将一个数逆序放入列表中，例如1234 ==》[4,3,2,1]
def parse_int(n,result=[]):
    if type(n) != int:
        n = int(n)

    if result == None:
        result = []

    if (n  > 0) and (n < 10):
        result += [n]
        return result
    else:
        return parse_int(n//10,result)


print(parse_int(1234))
#print(result)

def parse_int_by_for(n):
    if type(n) != int:
        n = int(n)
    result = []
    while(n >0):
        result += [n % 10]
        n = n // 10

    return result

print(parse_int_by_for(1234))


#猴子偷桃问题
def peach(days=10):
    if days == 1:
        return 1
    return (peach(days-1) + 1) * 2