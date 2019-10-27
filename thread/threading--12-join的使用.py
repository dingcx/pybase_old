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


def work():
    time.sleep(10)
    print('work')


def bar():
    threading.Thread(target=work).start()
    time.sleep(5)
    print('bar')


def foo():
    time.sleep(2)
    print('foo')


t = threading.Thread(target=foo,daemon=False,name='outer1')
t.start()


t1 = threading.Thread(name='worker',target=bar,daemon=True)
t1.start()
#
t1.join()

print('main thread exits')








