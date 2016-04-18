from faker import Faker
import logging
import random
import os
import time
logging.basicConfig(level=logging.INFO)
format_srt="""digraph main{
    node[shape=box,color=red]
    main[shape=diamond,color=blue]
    
    main -> init

    main -> nameline
    nameline ->"%s"
    //generated
    %s
}
"""

temp_format="""     "%s" -> "%s" 
    //the %d--%d 
"""
fake=Faker()
logging.info(fake.name())

number=50
people={}
sumsrt=''
sum_count=0
level=0.05
#first create a dictory of people
for i in range(number):
    people[i]=fake.name()



for i in range(number):
    for j in range(number):
        if(random.random()<level and i!=j):
            sumsrt=sumsrt+temp_format%(people[i],people[j],i,j)
            sum_count=1+sum_count
logging.info('sum_count:')
logging.info(sum_count)

#combine file
finnal=format_srt%(people[0],sumsrt)
file_name='generated_graph_'+str(int(time.time()))+'.gv'
#output *.gv
os.system('clean.cmd')
with open(file_name,'w') as f:
    f.write(finnal)
logging.info('----------compile---------')
#compile to png.
retcode=os.system("dot_compile.bat "+file_name+" png exit") 
logging.info(retcode)



