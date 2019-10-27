#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/20'
# code is far away from bugs with the god
'''
#set的实例化
s1 = set()
s2 = set(range(10))

print('s1',s1)
print('s2',s2)

#set的初始化
s1 = set()#定义一个空set
print('s1',s1)

s1 = set(range(5))
print('s1',s1)

s1 = set(list(range(10)))
print('s1',s1)


s1 = {}#这样生成的是一个字典
print('s1',type(s1))

#s1 = {,}不能像元组一样处理了。

s1 = {3,4,5}
print('s1',s1)


s1 = {(1,2),3,'a'}
print('s1',s1)

print('(1,2) 可以hash吗？',hash((1,2)))
#print('{1,2} 可以hash吗？',hash({1,2}))#不可hash
#print('[1,2] 可以hash吗？',hash([1,2]))#不可hash

#s1 = {[1],(1,),1}#不可hash
'''
set的元素要求：
    ①set的元素要求必须是可以hash
    ②list、set、dict都是不可hash的
    ③元素不可以被索引
    ④set可以迭代

set的增、改
add(elem)
    增加一个可以hash的元素到set中，如果存在就什么也不做

update(*others):集合并
    合并其他元素到set集合中来
    参数others必须是可迭代对象
    就地修改

remove(elem)
    删除元素，找不到就KeyError异常了

discard(elem)
    删除元素，找不到就不做操作

pop() ->item
    删除元素，并返回set中的任意元素，空的话报KeyError异常

clear()
    移除所有元素

'''

s1.add(1)
print('s1',s1)

s1.add(1)
print('s1',s1)

s1.update(s2)
print('s1',s1)


print('set pop()',s1.pop())
print('s1',s1)

print('-' * 30)
s2 = set(range(10,15))

s1.union(s2)
print('set union',s1)


'''
set的集合操作


集合的概念：
    全集：定义的一个范围的所有元素
    子集：A的所有元素都在B中，那么A就是B的子集
    

'''








