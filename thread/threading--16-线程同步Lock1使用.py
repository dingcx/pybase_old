#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/12'
# code is far away from bugs with the god
锁：凡是存在共享资源争抢的地方都可以使用锁，从而保证只有一个使用者可以完全使用这个资源

'''
import threading
from threading import Thread,Lock,RLock,Event,Semaphore,BoundedSemaphore,local
import  logging
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


cups = []#这个资源就被共享
lock = Lock()


def worker(total=100):
    logging.info('I am working')
    flag = False

    while True:
        lock.acquire()
        if len(cups) >= total:
            flag = True

        if not flag:
            time.sleep(0.0001)
            cups.append(1)

        lock.release()
        if flag:
            break


    logging.info(len(cups))


total = 1000

for i in range(10):
    t = Thread(target=worker,args=(total,),name='worker={}'.format(i))
    t.start()


print('================end=============')












