#!/bin/env python
#

import random

a = random.randint(0,10)

print(a)

if a > 5 :
    print('a greater than 5')
else:
    print('a less than 5')


def showplus(x):
    print(x)
    return x
    print(x + 1)
    print('-------')

showplus(4)
