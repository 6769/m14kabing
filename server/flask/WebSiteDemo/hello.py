# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:36:21 2015

@author: pip

@email:5pipitk@gmail.com
"""
import pdb
def application(environ, start_response):
    #pdb.set_trace()
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    #return [b'<h1>Hello, web!</h1>']
    return [str(environ).encode('utf')]