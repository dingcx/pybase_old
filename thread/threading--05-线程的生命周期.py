#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/6'
# code is far away from bugs with the god
'''
import threading
import time

def showthreadinfo():
    print("currentthread = {}".format(threading.current_thread()))
    print("main thread = {}".format(threading.main_thread()))
    print("active count = {}".format(threading.active_count()))


def worker():
    count = 0
    showthreadinfo()
    while True:
        if (count > 5):
            break
        time.sleep(1)
        count += 1
        print("I'm working")

t = threading.Thread(target=worker,name='worker1')
print(t.ident)
t.start()


while True:
    time.sleep(1)
    if t.is_alive():
        print('{} {} alive'.format(t.name,t.ident))
    else:
        print('{} {} dead'.format(t.name,t.ident))
        #t.start()
        '''线程只能被start()一次，其实很正常，一定一个线程装载进内存，那么就必须在线程的状态转换中不停的转换，除非已经消亡了。
           RuntimeError: threads can only be started once 
        '''



