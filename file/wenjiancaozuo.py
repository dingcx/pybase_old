#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/11'
# code is far away from bugs with the god
'''
f1 = open('test.txt','r+')
f1.write('start\n')

print(f1.name)
print(f1.tell())

#f1.seek(0,0)
print(f1.read())
f1.close()