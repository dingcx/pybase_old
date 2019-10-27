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

class MyThread(threading.Thread):
    def start(self):
        print('start================')
        super().start()

    def run(self):
        print('running=================')
        super().run()


t = MyThread(target=worker,name='worker1')

#t.start()
t.run()
'''
如果直接使用run，那么不会使用多线程启动线程函数，而是用start的话，会先调用start方法，然后再用run方法去创建子线程
'''
print(t.ident)

while True:
    time.sleep(1)
    if t.is_alive():
        print('{} {} alive'.format(t.name,t.ident))
    else:
        print('{} {} dead'.format(t.name,t.ident))

    break

