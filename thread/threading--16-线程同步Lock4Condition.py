#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/15'
# code is far away from bugs with the god
'''
import threading
from threading import Thread,Lock,RLock,Condition,Event,Semaphore,BoundedSemaphore,local
import logging
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = Event()
        self.cond = Condition()

    def produce(self,count=10):

        for i in range(count):
            self.data = random.randint(0, 100)
            with self.cond:
                self.cond.notify_all()
            self.event.wait(1)

    def cunsume(self):

        while True:
            with self.cond:
                self.cond.wait()
                self.event.wait(0.5)
                data = self.data
                logging.info(data)
                #self.data = None


d = Dispatcher()


p = Thread(target=d.produce,name='produce')

for i in range(3):
    Thread(target=d.cunsume,name='consume').start()

p.start()

print('============end============')