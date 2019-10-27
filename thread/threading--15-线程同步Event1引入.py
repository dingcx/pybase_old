#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/12'
# code is far away from bugs with the god
线程同步的几个概念：
    线程同步：就是线程间的协同，通过某种技术，让一个线程访问某些数据时，其他线程不能访问这些数据，直到该线程完成对数据的操作。
不同操作系统实现技术有所不同，有：
    临界区（Critical Section）
    互斥区（Mutex）
    信号量（Semaphore）
    事件（Event）
Python中同步的机制：
    ①Event（非常重要）：是线程间通信机制中最简单的实现，使用一个内部的标记flag，通过flag的True或FALSE的变化来进行操作
        set():标记设置为True
        clear():标记设置为False
        is_set():标记是否为True
        wait(timeout=None):设置等待标记为True的时长，None为无限等待，等到返回True，未等到超时时返回False
'''
from threading import Thread
import time

cups = []
flag = False


def worker(count=10):
    print("I am working")
    global flag
    while True:
        time.sleep(0.2)
        cups.append(1)

        if len(cups) >= count:
            flag = True
            break


def boss():
   global flag
   while True:
       time.sleep(1)
       if flag:
           print('good job')
           break


b = Thread(target=boss,name='boss')
w = Thread(target=worker,name='worker')

w.start()
b.start()

