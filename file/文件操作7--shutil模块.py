#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/5/13'
# code is far away from bugs with the god
'''
import shutil
from pathlib import Path

src = 'E:/test.txt'
dst = 'E:/testcp.txt'


p = Path(src)
p.write_text('abcde\nxyz\n123')


shutil.copy(src,dst)
#shutil.copytree()#这个函数可以去看看源码













