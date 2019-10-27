#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/9'
# code is far away from bugs with the god
def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
文件操作之open方法,关于模式
open的模式有三类，四项
    t:text,文本模式
    b:binary,二进制模式
    +:open中的模式区分得很清楚，无非就是读写，所以如果是是读权限加上了+，就会补充上写权限，
    这三类模式都依赖于其他四项模式存在的，
    r：读
    w：写
    x：create，创建文件并开始写
    a：追加写入
三类四项之间可以组合使用，例如：
    rt+:(默认的模式是t，可以省略），这表示读权限，附加上写权限，文本操作
    注意：r+模式下打开，文件指针放在首行,如果写入文件的话，会从该位置开始将内容覆盖写入



'''

f = open('test','w')
print(type(f))
print(f)

#print(f.read())

#write之后，不会立即写入，这和buffer有关
a = f.write('ssssssssss')


print(a)
f.close()


#x模式：如果文件已经存在，就会抛异常，x表示一定要自己创建文件
#f2 = open('test3','x')

#f2.write('fieunfn')

#f2.close()

#a模式：就是追加
f3 = open('test3','a')

f3.write('\n\tfffffffffff')
f3.close()


f4 = open('test','rb')

#while f4.
print(f4.read())

f4.close()

f5 = open('test_b','wb')

f5.write('教育'.encode('utf-8'))

f5.close()













