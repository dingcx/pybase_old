#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/7'
# code is far away from bugs with the god
'''
import threading
import time
import logging

FORMAT = "%(asctime)s %(threadName)s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

x = 0

class A:
    def __init__(self):
        self.x = 0

a = A()
a = threading.local()

def work():
    #x = 0
    global x
    a.x = 0
    time.sleep(0.0001)
    for _ in range(100):
        time.sleep(0.0001)
        a.x += 1
    logging.info(a.x)


for i in range(5):
    t = threading.Thread(target=work,name='w={}'.format(i))
    t.start()

print('==============')






