#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/6'
# code is far away from bugs with the god
关于线程退出的方式
    ①正常执行完
    ②抛出异常
'''
import threading
import time


def worker():
    count = 0
    while True:
        time.sleep(1)
        print("I'm working")
        print("Finish")

        count += 1
        if count > 5:
            #线程退出的方式
            #raise Exception('Thread error')
            #break
            return


t = threading.Thread(target=worker,name="worker2")
t.start()

#time.sleep(10)
print('=============end================')
