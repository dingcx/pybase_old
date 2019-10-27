#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/16'
# code is far away from bugs with the god
GIL是解释器进程级别的一把锁，全局解释器锁
GIL保证CPython进程中，只有一个线程执行字节码，甚至是在多核CPU的情况下，也是只能允许一个CPU上的一个线程在运行


在CPython中，由于GIL存在，使用多线程较为合理
在CPU密集型，使用多进程，要绕开GIL
Python中绝大多数内置数据结构的读写操作都是原子操作
由于GIL的存在，Python的内置数据类型在多线程编程的时候就编程了安全的了，但是实际上他们本身不是线程安全类型的
'''
import threading
from threading import Thread,Lock,RLock,Condition,Event,Semaphore,BoundedSemaphore,local,Barrier
import logging
import queue
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
