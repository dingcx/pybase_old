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


#2  类
class A:
    def __init__(self,environ,start_response):
        #self.html = b'<h1>丁常祥最帅</h1>' #这个b只能在默认的ASCII编码里面用
        self.html = bytes('<h1>丁常祥最帅</h1>','utf-8')
        print(environ, type(environ))
        print(start_response, type(start_response))
        self.start_res = start_response

    def __iter__(self):
        self.start_res('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        yield  self.html


#3.可调用对象、类定义
class Application:
    def __init__(self):
        self.content = b'dingcx.com'
        self.dcx = b'dcx'

    def __call__(self, environ, start_response):
        print(environ, type(environ))
        print(start_response, type(start_response))
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        return [self.content,self.dcx]


# server = make_server('localhost',9999,Application())
# server.serve_forever()

server = make_server('localhost',9999,A)
server.serve_forever()




