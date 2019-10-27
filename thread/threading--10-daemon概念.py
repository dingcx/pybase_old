#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/7'
# code is far away from bugs with the god
daemon在Linux中是守护进程（后台进程），但是这里的daemon不是这个意思

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
#t2 = MyThread(name='worker2',target=worker,daemon=f)

# 在线程start之前，可以使用setDaemon()方法来设置
# 当设置daemon为TRUE的时候，主线程会去检查工作线程的daemon状态，如果是True，主线程直接运行结束。
t1.setDaemon(True)

t1.start()
print('current daemon is {}'.format(threading.current_thread().daemon))
