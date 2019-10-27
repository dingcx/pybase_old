#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/8/25'
# code is far away from bugs with the god
'''
from wsgiref.simple_server import make_server,demo_app

server = make_server('localhost',9999,demo_app)
server.serve_forever()




