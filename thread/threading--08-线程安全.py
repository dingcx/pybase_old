#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/7'
# code is far away from bugs with the god
把这段代码放到ipython中去看看效果
'''
import threading


def worker():
    for x in range(100):
        print('{} is running'.format(threading.current_thread().name))


for x in range(1,5):
    name = 'worker={}'.format(x)
    t = threading.Thread(target=worker,name=name)
    t.start()

