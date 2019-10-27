#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/20'
# code is far away from bugs with the god
'''

#验证range这个对象是iterable还是iterator
r = range(10)
print('range\'s mro is ',r.__class__.mro())
print('range\'s dict is ',r.__class__.__dict__)
'''
range's dict is  {'__reduce__': <method '__reduce__' of 'range' objects>, '__ne__': <slot wrapper '__ne__' of 'range' objects>, '__new__': <built-in method __new__ of type object at 0x000000001D8ED190>, '__getattribute__': <slot wrapper '__getattribute__' of 'range' objects>, 'stop': <member 'stop' of 'range' objects>, '__contains__': <slot wrapper '__contains__' of 'range' objects>, '__iter__': <slot wrapper '__iter__' of 'range' objects>, '__doc__': 'range(stop) -> range object\nrange(start, stop[, step]) -> range object\n\nReturn an object that produces a sequence of integers from start (inclusive)\nto stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.\nstart defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.\nThese are exactly the valid indices for a list of 4 elements.\nWhen step is given, it specifies the increment (or decrement).', '__getitem__': <slot wrapper '__getitem__' of 'range' objects>, '__len__': <slot wrapper '__len__' of 'range' objects>, '__le__': <slot wrapper '__le__' of 'range' objects>, '__repr__': <slot wrapper '__repr__' of 'range' objects>, '__lt__': <slot wrapper '__lt__' of 'range' objects>, 'start': <member 'start' of 'range' objects>, 'count': <method 'count' of 'range' objects>, '__ge__': <slot wrapper '__ge__' of 'range' objects>, '__gt__': <slot wrapper '__gt__' of 'range' objects>, '__eq__': <slot wrapper '__eq__' of 'range' objects>, '__hash__': <slot wrapper '__hash__' of 'range' objects>, 'index': <method 'index' of 'range' objects>, '__reversed__': <method '__reversed__' of 'range' objects>, 'step': <member 'step' of 'range' objects>}

'''

#print(next(r))#TypeError: 'range' object is not an iterator








