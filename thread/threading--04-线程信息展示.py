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
showthreadinfo()
t.start()

print('=============end============')
print('=============end============')
print('=============end============')
print('=============end============')
print('=============end============')



