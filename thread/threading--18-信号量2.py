#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/15'
# code is far away from bugs with the god
信号量对象内部维护一个倒计数器，每次acquire都会减1，当acquire方法发现计数为0
就阻塞请求的线程，直到其他线程对信号量release后，计数大于0，恢复阻塞的线程
应用场景：
    连接池，因为资源有限，且开启一个连接成本高，所以使用连接池
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
print(sema.__dict__)

print(sema.acquire())
print(sema.acquire())
print(sema.acquire())

Thread(target=lambda s:s.acquire(),args=(sema,)).start()
time.sleep(2)
print(sema._value)

sema.release()
sema.release()
sema.release()
sema.release()


print(sema._value)


sema = BoundedSemaphore(3)

print(sema._value)
print(sema.__dict__)

print(sema.acquire())
print(sema.acquire())
print(sema.acquire())

Thread(target=lambda s:s.acquire(),args=(sema,)).start()
time.sleep(2)
print(sema._value)

sema.release()
sema.release()
sema.release()
sema.release()
#如果Semaphore的release次数超过了acquire的次数，不会报异常，
#使用BoundedSemaphore类，会记住初始值，这样就可以避免超界了
#查看sema.__dict__的值就可以看出来了。

print(sema._value)












