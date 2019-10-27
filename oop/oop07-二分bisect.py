#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/19'
# code is far away from bugs with the god
有一个无序序列[37,99,73,48,47,40,40,25,99,51],对其先排序输出新列表
分别尝试插入20,40,41到这个新序列中合适的位置，保证其有序
'''

origin = [37,99,73,48,47,40,40,25,99,51]
newlist = sorted(origin)

print(0,newlist)


#二分主要还是在查找的时候用
#25, 37, 40，假设要插入38
def insert_sort(orderlist,value):
    ret = orderlist[:]#得到25, 37, 40
    #print(ret)
    low = 0
    high = len(ret)#取得最低位和最高位

    while low < high:
        mid = (low + high) // 2  #每一次都和中间的数比较
        if orderlist[mid] < value:
            low = mid + 1  #因为上面的orderlist[mid]没有等于，所以这里可以跳过mid本省的再次比较
        else:
            high = mid
    ret.insert(low,value)

    return ret


lastlist = newlist

for x in (12,40,29,44):
    lastlist = insert_sort(lastlist,x)
    print(lastlist)

print(2,lastlist)


#Python有bisect模块
#使用二分法查询的前提是：有序
#核心是：折半至重合，时间复杂度是：O(log n)
import bisect


origin = sorted([37,99,73,48,47,40,40,25,99,51])

for i,x in enumerate(origin):
    print(i,x)


x = bisect.bisect(origin,40)
print(x)


x = bisect.bisect_left(origin,40)
print(x)


x = bisect.bisect_right(origin,40)
print(x)


bisect.insort_left(origin,40)
print(origin)


#练习，给定一个分值，判断其成绩的等级，这个方法很有趣
def is_abcd(sore):
    breakPoints = [60,70,80,90]
    grades = 'EDCBA'

    return grades[bisect.bisect(breakPoints,sore)]

print(is_abcd(89))