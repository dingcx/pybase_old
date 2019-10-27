#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god
'''

import pymysql


conn = None
cursor = None
insert_sql = "insert into reg (id,name,loginname,password) values(100,'sam1','sam1','sam1')"
select_sql = "select * from reg"

try:
    conn = pymysql.connect('192.168.179.129','root','root','test')
    print(conn)
    cursor = conn.cursor()
    cursor.execute(insert_sql)
    conn.commit()
    print(conn.ping(False))
except Exception as e:
    conn.rollback()
    print(e)
finally:
    if conn:
        conn.close()
    if cursor:
        cursor.close()



































