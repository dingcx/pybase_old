#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/8/25'
# code is far away from bugs with the god
'''
import sys,os

print(sys.path)

print(sys.argv,type(sys.argv))

print(sys.argv[0])#0是脚本本身


print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




