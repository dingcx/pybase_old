#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/6/15'
# code is far away from bugs with the god
'''
import threading
from threading import Thread,Lock,RLock,Condition,Event,Semaphore,BoundedSemaphore,local,Barrier
import logging
import time
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


