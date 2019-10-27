#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/15'
# code is far away from bugs with the god
信号量对象内部维护一个倒计数器，每次acquire都会减1，当acquire方法发现计数为0
就阻塞请求的线程，直到其他线程对信号量release后，计数大于0，恢复阻塞的线程
'''
import threading
from threading import Thread,Lock,RLock,Condition,Event,Semaphore,BoundedSemaphore,local,Barrier
import logging
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

sema = Semaphore(3)

print(sema._value)

print(sema.acquire())
print(sema._value)

print(sema.acquire())
print(sema._value)

print(sema.acquire())
print(sema._value)

#此时如果不release的话，再次acquire时，就会阻塞住线程
print(sema.release())
print(sema._value)

print('release之后',sema.acquire())
print(sema._value)

















