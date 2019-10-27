#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/7'
# code is far away from bugs with the god
多个线程就是一个进程中如果有多个线程，实现一种并发
'''
import threading
import time

def worker():
    count = 0
    while True:
        if (count > 5):
            break
        time.sleep(0.5)
        count += 1
        print('worker running')
        print(threading.current_thread().name,threading.current_thread().ident)


class MyThread(threading.Thread):
    def start(self):
        print('start================')
        super().start()

    def run(self):
        print('run==============')
        super().run()


t1 = MyThread(name='worker1',target=worker)
t2 = MyThread(name='worker2',target=worker)

t1.start()
t2.start()



