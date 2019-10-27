#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/27'
# code is far away from bugs with the god
可调用对象：
    定义一个类，并且实例化得到其实例，并将实例像函数一样使用，这就是可调用对象呢

'''

def foo():
    print()


print(foo)
print(foo.__dict__)
print(foo.__call__)

#判断是否可调用
print(callable(foo))



class A:
    def __call__(self, *args, **kwargs):
        print('call')
        print(*args)
        #解构的话，一定是函数本身有定义对应的key-word-only
        #print(**kwargs)
        print(kwargs)

#__call__绑定的是self
a = A()
a()
#a(1,2,3,4,sep=' ', end='\n')
a(1,2,3,4,x=1, y=4)

class B:pass

#说明如果没有定义__call__,那么这个类的对象是不可调用的
print("callable(B)?--->",callable(B()))


class Fib:
    def __init__(self):
        #使用缓存，减少计算
        self.items = [0,1,1]#索引和数列的索引保持一致，0只是过渡，不代表数列中的项

    def __call__(self, index):#第三项为2
        if index < 0:#对负索引的处理
            raise  IndexError("Wrong Index")
        if index >= len(self.items):
            for i in range(len(self) + 1,index + 1):
                self.items.append(self.items[i - 1] + self.items[i - 2])
        return self.items[index]
        #return self.items[1:]
        #return self.items[1:index+1]

    def __getitem__(self, index):#将对象变成了一个可迭代对象

        return self(index)

    def __len__(self):
        return len(self.items) - 1

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return str(self.items)

    __repr__ = __str__


fib = Fib()
#Fib()(10)这个的返回值是__call__的返回值
print(fib(10))
print(fib(1))
print(fib[9])

for i in enumerate(fib):
    print(i)

print('-------fib(15)---------------')
fib(15)
for i in enumerate(fib):
    print(i)


