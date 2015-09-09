# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:31:33 2015

@author: pip

@email:5pipitk@gmail.com
"""

import time
from flask import Flask, request, render_template,abort,make_response

import zjuocr
apilist=dict(zjuocr=zjuocr,)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/api',methods=['GET', 'POST'])
def apihome():
    return render_template('apihome.html')

@app.route('/api/<apiname>',methods=['GET', 'POST'])
def apinterface(apiname):
    if apiname in apilist.keys():
        resultofapi=callthisapi(apiname,request)
        
        reTurnHttpResponse=make_response(resultofapi)
        reTurnHttpResponse.headers['Access-Control-Allow-Origin']='*'
        reTurnHttpResponse.headers['Access-Control-Allow-Methods']='GET,POST,OPTIONS'
        reTurnHttpResponse.headers['Access-Control-Allow-Headers']='X-Requested-With'
        reTurnHttpResponse.headers['Generate-Time']=time.ctime()
        return reTurnHttpResponse
    else:
        return 'This API:%s doesn\'t exitsted in pipi\' code'%apiname
    

def callthisapi(apiname,request):
    acceptable_para=apilist[apiname].info.para
    para_must=apilist[apiname].info.para_must
    actualfunction=apilist[apiname].info.function
    
    get_in_request=[]
    for i in acceptable_para:
        i_res=None
        
        try:
            i_res=request.args.get(i, '')
            get_in_request.append(i_res if i_res else None)
        except:
            pass
    paradict=dict(zip(acceptable_para, get_in_request  ))
    for i in para_must:
        if paradict.get(i)==None:
            return 'Vital Paragrams missed'
    
    apireturn=actualfunction(paradict)
    
    return apireturn
        
            

#                           
@app.route('/admin',methods=['GET'])
def adminpage():
    try:
        passkey=request.args.get('im_admin','')
    except:
        abort(404)
    if passkey!='5pipi':
        abort(404)
    else:
        return "Welcome to admin page,hhhh!"
    

@app.route('/40x',methods=['GET','POST'])
def bannedpage():
    abort(404)
    

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning('log-waring:404')
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'Page Generate Time:%s'%time.ctime()
    return resp

if __name__ == '__main__':
    app.debug=True
    app.run()#args  : host='0.0.0.0'