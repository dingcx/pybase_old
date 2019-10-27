#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/4'
# code is far away from bugs with the god
线程是解决高并发的方法之一（多进程、多线程、协程）
'''
import threading
import  time


def worker():
    time.sleep(10)
    print("I'm working")
    print("Finish")


t = threading.Thread(target=worker,name='worker1')
t.start()

#time.sleep(10)#注意这里加没加注释的区别
print('============end=======================')














