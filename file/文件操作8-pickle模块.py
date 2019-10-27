#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/15'
# code is far away from bugs with the god
'''
import pickle

i = 99
s = 'abc'
l = {'a':0x111111,'b':'abcd','c':[1,2,3]}

with open('testpickle','wb') as f:
    pickle.dump(i,f)
    pickle.dump(s,f)
    pickle.dump(l,f)



print('-'*30)

with open('testpickle','rb') as f:
    '''
        for i in f:
        tmp = pickle.load(f)
        print(type(tmp),tmp)
        #真正要进行循环输出的话，可能只能用while了，而且必须结合异常处理来使用
    '''
    tmp = pickle.load(f)
    print(type(tmp),tmp)
    tmp = pickle.load(f)
    print(type(tmp), tmp)
    tmp = pickle.load(f)
    print(type(tmp), tmp)

    #print(type(pickle.load(f)))



class AA:
    def show(self):
        print('abc')

a = AA()
print(a)

with open('testpickle','wb') as f:
    pickle.dump(a,f)

with open('testpickle','rb') as f:
    tmp = pickle.load(f)
    print(type(tmp),tmp)
    tmp.show()#这里就把对象给恢复出来了






