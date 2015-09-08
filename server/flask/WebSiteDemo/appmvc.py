# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:44:13 2015

@author: pip

@email:5pipitk@gmail.com
"""
import time
from flask import Flask, request, render_template,abort,make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    searchword = request.args.get('q', '')
    print(searchword)
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', 
                           message='Bad username or password', username=username)
                           

@app.route('/40x',methods=['GET','POST'])
def bannedpage():
    abort(404)
    

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning('log-waring')
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'Page Generate Time:%s'%time.ctime()
    return resp

if __name__ == '__main__':
    #app.debug=True
    app.run()#args  : host='0.0.0.0'