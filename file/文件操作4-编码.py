#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/11'
# code is far away from bugs with the god

'''
f = open('test_t.txt')


def test():
    #f = 54
    with f:
        print(f.fileno())
        print(f.closed)

        return
        print('_____________')

test()

print(f.closed,'!!!!!!!!!!!')

a = 200

with open('test_t.txt') as f:
    a = 100
    print(f.read())

print(f.closed,'!!!!!!!!!!!!!!!!!','a',a)


