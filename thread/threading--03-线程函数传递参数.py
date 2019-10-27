#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/6'
# code is far away from bugs with the god
如果给线程函数传递参数
'''
import threading
import time


def worker(x,y):
    count = 0
    while True:
        time.sleep(1)
        print("I'm working")
        print("Finish")

        count += 1
        if count > x:
            #线程退出的方式
            #raise Exception('Thread error')
            #break
            return

#给线程函数传递参数其实就是通过位置参数和键值对参数进行传递
#t = threading.Thread(target=worker,name="worker2",args=(4,0))
t = threading.Thread(target=worker,name="worker2",args=(4,),kwargs={'y':None})
t.start()

#time.sleep(10)
print('=============end================')
