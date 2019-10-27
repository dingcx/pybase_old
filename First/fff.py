#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/2'
# code is far away from bugs with the god
'''


n = 4
Triangle = [0,1,0]
print('开始了')
print(Triangle)


print("----------------")
for i in range(1,n+1) :
    S = Triangle[i - 1]
    Line = [0]
    CL = []
    if i % 2 == 1:
        CL = []
        for j in range((i+1) // 2 ) :
            #S = Triangle[i - 1]
            Su = S[j] + S[j + 1]
            Line.append(S)
            CL.append(Su)
        CL.append(0)
        NL = Line + CL
    else :
        for j in range(i//2 + 1) :
            JSU = S[j] + S[j + 1]
            Line.append(JSU)
            if j != 0 :
                CL.append(JSU)
        CL.append(0)
        NL = Line + CL
Triangle.append(NL)
print(Triangle)