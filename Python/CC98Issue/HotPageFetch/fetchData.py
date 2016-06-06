# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:59:52 2016

@author: pip5
"""

import requests
import os
import sys
import sqlite3
import logging
from functools import  reduce
from json import JSONDecodeError
#later put config to config.cfg file to split logic and specific command.
SQLITE3DATABASENAME='cc98.db'
URL="http://api.cc98.org/Topic/Hot"
DELAYTIME=30


def constructureUpdate(pairOfdata):
    strformat_int=' %s=%d '
    strformat_str=" %s='%s' "
    if type(pairOfdata[1])==int:
        res=strformat_int%(pairOfdata)
    else:
        res=strformat_str%(pairOfdata)
    return res

class fetchAndWrite(object ):
    def __init__(self,url,sqlite3DatabaseName,delaytime):
        self.url=url
        self.sqlite3DatabaseName=sqlite3DatabaseName
        self.delaytime=delaytime
        self.hotdata=None
        self.DBfileExist=False
        self.conn=None
        self.cursor=None
        self.checkedDBmark=False
        #just fetch hot pages
    def fetch_hotpage(self):
        """
        Fetch hotpage used json to dict,from the http://api.cc98.org
        return dict(json)        
        """        
        
        hotpage=requests.get(self.url)
        self.hotdata=hotpage.json()#in a list,sorted by Index.
        return self.hotdata
    def checkDBFilexist(self):
        currentDir=os.listdir()
        if self.sqlite3DatabaseName in currentDir:
            #db in the list
            return True
        else:
            return False
    def createDB(self):
        #init DB's table 
        self.conn = sqlite3.connect(self.sqlite3DatabaseName)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""create table hotpage (
                        id          int not null,
                        hotRank     int         ,
                        hitCount    int not null,
                        boardid     int not null,
                        boardName    varchar(30) not null,
                        authorName   varchar(30),
                        replyCount   int not null,
                        participantCount int not null,
                        title        varchar(110) not null,
                        createTime   varchar(20) not null,
                        primary key(id)          );""")
        self.cursor.close()
        self.conn.close()
    def constructQuery(self,targetDict):
        if targetDict['authorName']==None:
            targetDict['authorName']='null'
        keys=targetDict.keys()
        valuses=targetDict.values()
        #column_name=reduce( lambda x,y:x+','+y , keys)
        column_name=str(tuple(keys)).replace("'","")#all with "(xxxx)"
        valuses_data=str(tuple(valuses))
        return (column_name,valuses_data )
        
    def insertDB(self,oneQuery):
        #string format
        
        #constructure sql 
        readyforinsert=self.constructQuery(oneQuery)
        self.cursor.execute("insert into hotpage %s values %s"%readyforinsert)
        
    
    def searchDB(self,oneQuery):
        #search str
        self.cursor.execute('select id from hotpage where id==?', 
                           (oneQuery['id'],)
                           )
        sql_result=self.cursor.fetchall()
        if sql_result==[]:
            #represent not exist in DB
            return False
        else:
            return sql_result
            
            
    def updateDB(self,oneQuery):
        whereid=oneQuery['id']
        del oneQuery['id']
        keys=oneQuery.keys()
        values=oneQuery.values()
        newpair=tuple(   map(constructureUpdate,zip(keys,values))      )
        
        self.cursor.execute(
            'update hotpage set %s where id==?'%("%s,%s,%s,%s,%s, %s,%s,%s,%s"%newpair),
                           (whereid,))
        
        
    def writeLogicDB(self):
        self.conn=sqlite3.connect(self.sqlite3DatabaseName)
        self.cursor = self.conn.cursor()
        for i in range(len(self.hotdata)):
            perPost=self.hotdata[i]
            perPost['hotRank']=i+1
            if self.searchDB(perPost):#this query has existed in the DB.
                self.updateDB(perPost)
            else:
                self.insertDB(perPost)
        
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
    def runOnce(self):
        try:
            self.fetch_hotpage()
            for i in self.hotdata:
                logging.info(i['createTime']+'\t'+i['title'])
        except JSONDecodeError as e:
            logging.info('[-]JSONDecodeError:%s'%e)
            return -1
        except :
            logging.info('[-]OtherError')
            return -2
        if self.checkedDBmark==False:
            if self.checkDBFilexist()!=True:
                self.createDB()
            self.checkedDBmark=True
        self.writeLogicDB()
        return True
            
        
 

if __name__=='__main__':
    fetchcore=fetchAndWrite(URL,SQLITE3DATABASENAME,DELAYTIME)
    fetchcore.runOnce()