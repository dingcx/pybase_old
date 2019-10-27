#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/15'
# code is far away from bugs with the god
'''
import threading
from threading import Thread,Lock,RLock,Condition,Event,Semaphore,BoundedSemaphore,local,Barrier
import logging
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

barrier = Barrier(3)


def worker(bar:Barrier):
    print('I am working',bar.n_waiting)
    bar.wait()
    print('finish my job.',bar.n_waiting)

ts = []

for i in range(2):
    t = Thread(target=worker,args=(barrier,))
    t.start()
    ts.append(t)


print('==============end================')


while True:
    time.sleep(1)
    print(barrier.n_waiting)


