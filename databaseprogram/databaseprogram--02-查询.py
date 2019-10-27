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

select_sql = "select * from user"

try:
    conn = pymysql.connect('localhost','root','root','sakila')
    print(conn)
    cursor = conn.cursor()
    cursor.execute(select_sql)
    rows = cursor.fetchone();
    print(type(rows))
    print(rows)
    print(cursor.rowcount,cursor.rownumber)


except Exception as e:
    conn.rollback()
    print(e)
finally:
    if conn:
        conn.close()
    if cursor:
        cursor.close()



































