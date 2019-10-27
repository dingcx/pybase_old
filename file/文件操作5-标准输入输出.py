#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/12'
# code is far away from bugs with the god
'''

from sys import stdout,stdin,stderr

f = stdout

print('stdout的本质是',f,'类型是：',type(f))
print('stderr的本质是',stderr,'类型是：',type(stderr))

f.write('abcdd\n')
print('12423222222222222')

stderr.write('zzzzzzzzzzzdyen\n')


stdin.read(stderr.write('zzzzzzzzzzzdyen\n'))




