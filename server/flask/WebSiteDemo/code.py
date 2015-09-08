# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:13:04 2015

@author: pip

@email:5pipitk@gmail.com
"""


import web
urls=(
'/','index'
)
#app = web.application(urls, globals())
class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    assert 0,"ImportError: No module named 'BaseHTTPServer"
    app = web.application(urls, globals())
    app.run()
