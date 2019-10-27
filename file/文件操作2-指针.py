#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/11'
# code is far away from bugs with the god
#文件操作指针
TextIOBase类中的指针操作（其实就是字符打开的文件）
seek(offset[, whence])
    seek方法的作用：使用给定的offset来改变stream的位置--就是文件指针。seek的运行靠whence参数来决定,默认的值位SEEK_SET
    Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.
    whence的取值：
        SEEK_SET或者0：从文件流开始位置seek，这也是函数的默认值，offset必须是TextIOBase.tell()的返回值和0两者之一
        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset value produces undefined behaviour.
        SEEK_CUR或者1：seek到当前位置（position = tell（）），offset参数必须为0，这其实就不做任何操作，并且该whence下，offset不支持其他值
        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).
        SEEK_END或者2：seek到文件结束的位置，offset必须为0，其他值不支持
        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).
    Return the new absolute position as an opaque number.返回一个改变后位置的值
    New in version 3.1: The SEEK_* constants.
其实说白了，只有使用SEEK_SET来设置文件位置之外，其他的取值其实没有什么意义
    SEEK_CUR:如果我们不知道当前位置在哪里，那么SEEK_CUR是一个选择，但是为什么不用tell()呢？
    SEEK_END:这个可以帮助我们快速定位到文件尾部

如果是以字节文件打开的话，就不一样了
seek(offset[, whence])
    作用和字符的是一样的
    Change the stream position to the given byte offset. offset is interpreted relative to the position indicated by whence. The default value for whence is SEEK_SET. Values for whence are:

    SEEK_SET或者0：从文件流开始位置，也是默认的模式，偏移量必须是整数或者0,0表示从文件首部开始
    SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive
    SEEK_CUR或者1：当前的文件流位置，偏移量可以为负数
    SEEK_CUR or 1 – current stream position; offset may be negative
    SEEK_END或者2：文件尾部，偏移量总是为负数（要么就是0）
    SEEK_END or 2 – end of the stream; offset is usually negative
    Return the new absolute position.

    New in version 3.1: The SEEK_* constants.
    New in version 3.3: Some operating systems could support additional values, like os.SEEK_HOLE or os.SEEK_DATA. The valid values for a file could depend on it being open in text or binary mode.

'''
import os

#r模式是只读模式打开文件，r+模式下打开，文件指针放在首行,如果写入文件的话，会从该位置开始将内容覆盖写入
f1 = open('test_point.txt','r+')
f1.write('sssssssddeeding\n')
#f1.flush() #什么时候需要使用flush，什么时候不用呢？
print(f1.name)
print(f1.tell())

#通过实验知道，文件偏移可以可以到任意位置，只要重置了文件指针的位置，就会从该位置开始读写，写入的时候如果之前的位置没有写入任何
# 值，将会写入二进制的NULL。
print(f1.seek(116,0))
print('文件写入数据量为：',f1.write('eeeeeeeeeeeeeee'))
str = f1.read()
#print(str)
print(f1.tell())
f1.close()

f2 = open('seek1.txt','w+');
print('w+模式打开时，文件指针位置为：',f2.tell()) #从0开始
print('写入数据量为：',f2.write('4djfnudneudhd'))
print('文件写入之后，文件指针的位置：',f2.tell())
print('whence使用SEEK_SET来设置文件指针位置')
print('seek之后的文件指针位置为：',f2.seek(0,os.SEEK_SET),f2.tell())
print('whence使用SEEK_CUR来设置文件指针位置')
print('seek之后的文件指针位置为：',f2.seek(0,os.SEEK_CUR),f2.tell())
print('whence使用SEEK_END来设置文件指针位置')
print('seek之后的文件指针位置为：',f2.seek(0,os.SEEK_END),f2.tell())
f2.close()

#追加的模式打开文件，即便文件不存在，会创建文件,这个实验主要是为了看看在a模式下打开文件，调整文件指针，是怎么写入的
#实验证明：在追加模式下，即便你调整了文件指针的位置，最终写入的位置也是在文件尾部
f3 = open('testr3.txt','a+')
#a模式下打开文件，文件指针位置在文件尾部
print('a模式下打开文件时文件指针的位置:',f3.tell())
print('文件写入数据量为：',f3.write('dddddddduebgue\n'))
print('调整文件指针后，文件指针的位置:',f3.seek(0,os.SEEK_SET))
f3.write('test append mode')
print('写入之后，文件指针的位置：',f3.tell())
f3.close()

f4 = open('test3','rb+')
print('t模式下打开的文件类型',f2)
print('b模式下打开的文件类型',f4)
print('当前文件指针的位置：',f4.tell())
print(f4.read())
print('调整文件位置：',f4.seek(-10,os.SEEK_CUR))
print('调整文件位置：',f4.seek(-10,os.SEEK_END))
f4.close()










