# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:31:55 2015

@author: pip

@email:5pipitk@gmail.com
"""

import time
count=0
while count<1000000:
    count+=1
    cursor.execute('select * from user where id=?','2')
    time.clock()
waitt=time.clock()
print(count/waitt)