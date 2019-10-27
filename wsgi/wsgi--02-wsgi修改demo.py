#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/8/25'
# code is far away from bugs with the god
'''
from wsgiref.simple_server import make_server,demo_app

response_string = b'www.dingcx.com'

#1、提供function
def application(environ,start_response):
    print(environ,type(environ))
    print(start_response,type(start_response))
    start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    return [response_string]


server = make_server('localhost',9999,application)
server.serve_forever()




