# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:59:52 2016

@author: pip5
"""
import time
import fetchData
import logging
logging.basicConfig(filename='tempKeepRun.py.log',level=logging.INFO)


SQLITE3DATABASENAME='cc98.db'
URL="http://api.cc98.org/Topic/Hot"
DELAYTIME=30

def tempRunPerDeltaT(delayMin):
    app=fetchData.fetchAndWrite(URL,SQLITE3DATABASENAME,DELAYTIME)
    while(1):
        app.runOnce()
        #for i in app.hotdata:
        #    logging.info(i['createTime']+'\t'+i['title'])
        logging.info("[+]LocalTime:%s"%time.ctime())
            
            
        time.sleep(delayMin*60)

if __name__=='__main__':
    tempRunPerDeltaT(30)