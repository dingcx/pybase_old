#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/7'
# code is far away from bugs with the god
'''
import threading
import logging #默认级别是警告，info低于警告

def worker():
    for x in range(100):
        logging.warning('{} is running'.format(threading.current_thread().name))


for x in range(1,5):
    name = 'worker={}'.format(x)
    t = threading.Thread(target=worker,name=name)
    t.start()

