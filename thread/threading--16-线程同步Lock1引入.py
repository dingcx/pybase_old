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

def worker(total=100):
    logging.info('I am working')

    while True:

        if len(cups) >= total:#这里判断的时候，很可能不同的线程切换的时候得到True，但是临界点就一个。
            break

        time.sleep(0.1)
        cups.append(1)

    logging.info(len(cups))


total = 1000

for i in range(10):
    t = Thread(target=worker,args=(total,),name='worker={}'.format(i))
    t.start()


print('================end=============')












