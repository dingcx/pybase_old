#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/2'
# code is far away from bugs with the god
生成器
'''
g1 = (i for i in range(5))

def fn(n):
    for i in range(n):
        yield i

print(type(fn))
print(type(fn(5)))

print(next(fn(5)))

def gen():
    print("line 1")
    yield 1
    print("line 2")
    yield 2
    print("line 3")
    return 3

g = gen()
next(g)

#其实next就是去查迭代器里面的下一个yield
next(g)
#next(g)


def inc():
    def counter():
        i = 0;
        while True:
            i += 1
            yield i

    c = counter()

    def _inc():
       return  next(c)

    return _inc

g = inc()
print(g())
print(g())

#斐波拉契的生成器版本
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        yield a,b #yield只要是合法的值，都可以


for x in fib(10):
    print(x)


#协程的举例
def g1():
    for i in range(5):
        yield i


def g2():
    for i in 'abcde':
        yield i

gen1 = g1()
gen2 = g2()

'''
输出结果为：
0
a
1
b
2
c
3
d
4
e

'''
for i in range(5):
    print(next(gen1))
    print(next(gen2))



#yield from语句

def inc():
    for x in range(1000):
        yield x

#与上面的是等价的
def inc():
    yield from range(1000)




def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc


fn1 = counter(5)
fn2 = counter(5)

print(fn1 == fn2)
print(fn1 is fn2)


def sort(iterable):
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):#?????
            print(i,y)
            if x > y:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)

    return newlist

print(sort([1,2,3]))

sorted()

