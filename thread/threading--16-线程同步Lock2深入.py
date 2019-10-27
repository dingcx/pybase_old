#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/13'
# code is far away from bugs with the god
'''
import threading
from threading import Thread,Lock
import time


class Counter:
    def __init__(self):
        self._val = 0
        self.lock = Lock()

    @property
    def value(self):
        with self.lock:
            return self._val

    def inc(self):
        self.lock.acquire()
        try:
        #赋值语句是可以被打断的,这样就是一个线程安全的类
            self._val += 1
        finally:
            self.lock.release()

    def dec(self):
        with self.lock:
            self._val -= 1


lock = Lock()


def run(c:Counter,count=100):
    for _ in range(count):
        for i in range(-50,50):
            #判断这边是不会被打断的，对于局部变量来说，是线程安全的
            if i < 0:
                c.dec()
            else:
                c.inc()


c = Counter()
c1 = 10
c2 = 1000


for i in range(c1):
    Thread(target=run,args=(c,c2)).start()

e = threading.Event()

while not e.wait(1):

    if threading.active_count() == 1:
        print(c.value)
        e.set()
    else:
        print(threading.enumerate())

print('====================end==================')

