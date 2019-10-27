#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/11'
# code is far away from bugs with the god
#缓冲区的使用
def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
'''

import io


print('系统默认的缓冲区大小是：',io.DEFAULT_BUFFER_SIZE)
#系统默认的缓冲区大小是： 8192

#二进制模式下
f1 = open('test4.txt','w+b')
f1.write('dingcx.com'.encode())
print('此时肯定是读不到内容的，因为文件指针在文件尾部:',f1.read())

#如果移动了文件指针，那么就会将缓冲区中的数据写入到磁盘中
f1.seek(0,io.SEEK_SET)
print('此时再读文件呢？:',f1.read())
print('好像并没有用到缓冲区呢？:')


f1.flush()
f1.close()


#使用行缓冲，也就是说遇到了/n换行符，就会将字符写入到磁盘中
f2 = open('test_t.txt','w+',1)
f2.write('dcx')
f2.write('dcx' * 4)

tmp_f = open('test_t.txt','r+')
print('此时读取文件中的内容:',tmp_f.read())
tmp_f.close()

f2.write('\n')

tmp_f = open('test_t.txt','r+')
print('此时再读取文件中的内容:',tmp_f.read())
tmp_f.close()

#和行缓冲一块的数据也会被刷新到磁盘中
f2.write('Hello\nPython')

tmp_f = open('test_t.txt','r+')
print('此时再再读取文件中的内容:',tmp_f.read())
tmp_f.close()

f2.close()




