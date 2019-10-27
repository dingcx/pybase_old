#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/9/26'
# code is far away from bugs with the god
'''


class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return '<Node {} {}>'.format(self.item,self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,item):pass
        #node =

    def iternodes(self):
        pass

ll = LinkedList()
ll.append(1)















