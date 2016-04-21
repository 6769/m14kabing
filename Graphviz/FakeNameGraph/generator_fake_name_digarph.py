from faker import Faker
import logging
import random
import os
import time
logging.basicConfig(level=logging.INFO)


format_srt="""digraph main{
    node[color=red]
    main[shape=diamond,color=blue]
    //node feature
    %s
    
    main -> nameline
    nameline ->"%s"
    //generated
    %s
}
"""
#for node attributes
temp_format_node="""
    "%s"[color=%s]
"""

#for edge attributes
temp_format_edge="""
    "%s" -> "%s"[color=%s]
    //the %d--%d
    """
    
fake=Faker()
logging.info(fake.name())

colorlist=['red','blue','yellow','black','green','gray',
            'lightblue','orange','purple','brown','cyan',
            'darkgreen','gold',]
number=30
people={}
sumsrt=''
sumsrt_node=''
sum_count=0
level=0.07
#first create a dictory of people
for i in range(number):
    people[i]=fake.name()

for i in range(number):
    the_color=random.choice(colorlist)
    sumsrt_node=sumsrt_node+temp_format_node%(people[i],random.choice(colorlist))
    for j in range(number):
        if(random.random()<level and i!=j):
            sumsrt=sumsrt+temp_format_edge%(people[i],people[j],the_color,i,j)
            sum_count=1+sum_count
            
            
logging.info('sum_count:')
logging.info(sum_count)

#combine file
finnal=format_srt%(sumsrt_node,people[0],sumsrt)
file_name='generated_graph_'+str(int(time.time()))+'.gv'

#output *.gv
os.system('clean.cmd')
with open(file_name,'w') as f:
    f.write(finnal)
logging.info('----------compile---------')

#compile to png.
retcode=os.system("dot_compile.bat "+file_name+" png exit") 
logging.info(retcode)



