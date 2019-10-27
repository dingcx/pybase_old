#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/13'
# code is far away from bugs with the god
RLock是一个线程相关的锁，某个线程如果要获得这个锁，必须是count=0的时候，
'''
import threading
from threading import Thread,Lock,RLock,Condition,Event,Semaphore,BoundedSemaphore,local
import logging
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


cups = []
lock = RLock()


print(1,lock)

lock.acquire()

print(2,lock)

lock.release()
print(3,lock)


def sub(l):
    logging.info('~~~~~~~~~~~~~~~~~in sub thread')
    l.acquire()
    print('sub',lock)
    l.release()
    logging.info('~~~~~~~~~~~~~end sub')

t = Thread(target=sub,args=(lock,))
t.start()

time.sleep(2)
lock.acquire()#观察这两个的区别，如果是阻塞的，那么整个主线程就卡住了。
#lock.acquire(False)
print(4,lock)
print('============end============')




