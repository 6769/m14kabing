# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:29:19 2015

@author: pip

@email:5pipitk@gmail.com
"""

from multiprocessing import Pool
import os, time
import requests


#N=500

def multiGet(addr):
    res=requests.get(addr)
    return res.content.decode()

def maintask( host="http://127.0.0.1:5000/",N=500):
    """
    host:addr to fetch
    N:     concurrency
    """
    print('Parent process %s.' % os.getpid())
    print('Target:%s---Concurrency:%d'%(host,N))
   
    p = Pool(5)
    starttime=time.time()#start timer
    try:
        for i in range(N):
            p.apply_async(multiGet, args=(host,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
    except Exception:
        print('some error')
    endtime=time.time()
    print('All subprocesses done.')
    print('Time spend:%.2f s'%(endtime-starttime))
    print('Average cost:%.1f/s'% (N/(endtime-starttime)))

if __name__=='__main__':
    maintask(N=10000)