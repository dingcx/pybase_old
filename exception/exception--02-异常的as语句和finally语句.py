#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/25'
# code is far away from bugs with the god
异常的as子句
    被捕获的异常，应该是异常的实例，那么在except语句块中怎么去使用这个异常呢？这就是as子句的由来。
    捕获的这个异常的生命周期只在except语句块中
异常的finally语句：
    不管捕获到或者没有捕获到异常，都会执行finally语句块中的语句
    在finally语句块中，还可以捕获异常（为什么有这个必要，因为f.close一样会抛出异常的）
'''


class MyException(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message


try:
    raise MyException(200,'OK')
    #raise MyException  #如果raise语句后面直接跟着的是类名，那么会去找默认的异常类的构造器，显然，这个类中没有默认的构造器
except MyException as e:
    print('MyException = {} {}'.format(e.code,e.message))
except Exception as e:
    print('Exception = {}'.format(e))


print('从异常中联想到了重载的问题。。。。。。。。。。')


'''
Python中的重载是用来默认的参数列表来实现
'''


class MyException(Exception):
    def __init__(self,code=None,message=None):
        self.code = code
        self.message = message


try:
    #raise MyException(200,'OK')
    raise MyException  #如果raise语句后面直接跟着的是类名，那么会去找默认的异常类的构造器，显然，这个类中没有默认的构造器
except MyException as e:
    print('MyException = {} {}'.format(e.code,e.message))
except Exception as e:
    print('Exception = {}'.format(e))
#验证e的生命周期在except块内
#print('MyException = {} {}'.format(e.code,e.message))

f = None

try:
    f = open('test.txt')
except Exception as e:
    print('{}'.format(e))
finally:
    print('进行清理工作')
    if f:
        print('进来了')
        f.close()

#在finally语句块中捕获异常
f = None

try:
    f = open('test.txt')
except Exception as e:
    print('{}'.format(e))
finally:
    print('进行清理工作')
    if f:
        try:
            f.close()
        except NameError as e:
            print(e)

print('finally执行时机...............')
#finally执行时机
def foo():
    try:
        return 3
    finally:
        print('finally')
    print('========')

print(foo())


import sys

def foo():
    #如果这边返回的话，根本就不会到try语句块中
    # return 1
    try:
        sys.exit(1)
        #return 3
    finally:
        # 如果是这里返回的话，这个有点意思
        # 当进入try后，执行return 3,但是finally一定要执行
        return 5
    print('==========')


print(foo())
'''
总结：
首先，在程序没有异常的情况下，首先执行到try里面的语句，但是只执行到了return里面的expression，expression首先存放在操作数栈顶，然后复制到局部变量区，并没有执行返回语句return（执行返回语句通常意味着程序执行结束）。然后执行finally，当执行到finally里面的return时候，会将return语句执行完整，此时程序已经有了返回值，因为，执行结束。

总结：执行try块，执行到return语句时，先执行return的语句，但是不返回到main 方法，接下来执行finally块，遇到finally块中的return语句，执行,并将值返回到main方法，这里就不会再回去返回try块中计算得到的值

'''
