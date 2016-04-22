import requests
import logging
import re
from functools import reduce 
logging.basicConfig(level=logging.INFO)

sina_shorturl='http://t.cn/'
test_url='http://t.cn/RqC4kYg'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
relink = 'HREF="(.*)">'
url_pattern=re.compile(relink)

low_case_alpha=[chr(i) for i in range(97,123)] #abcdefgh...
upper_case_alpha=[chr(i) for i in range(65,91)]#ABCDEFGH...
number_alpha=[str(i) for i in range(0,10)]

transfer_table=low_case_alpha+upper_case_alpha+number_alpha
transfer_table_len=len(transfer_table)
transfer_table_dict=dict(zip(list(range(transfer_table_len)),transfer_table))
transfer_table_dict_reversed=dict(zip(transfer_table,list(range(transfer_table_len))))

def xtoint(numberlist,base):
    cout=0
    for i in range(len(numberlist)):
        cout=cout+base**i*int(numberlist[i])
    return cout
def inttox(number,base):
    if(number>=1):
        bit_m=number%base
        next_bit=(number-bit_m)/base
        return [bit_m,]+inttox(next_bit,base)
    else:
        return []
class Gen_url(object):
    def __init__(self,start_surfix='RqC4k0M'):
        self.starter=start_surfix
        self.output=''
        self.maplist=list(start_surfix)
        self.maplist.reverse()# for easy to use i in range
        self.url_length=len(start_surfix) if start_surfix!='' else 1
        self.counter_list=list(map(lambda x:transfer_table_dict_reversed[x]
                                ,self.maplist))
        self.counter_urllength_radix=xtoint(self.counter_list,transfer_table_len)
    def get_next(self):
        self.counter_urllength_radix=self.counter_urllength_radix+1
        self.counter_list=list(
            map(int,inttox(self.counter_urllength_radix,transfer_table_len))
            )
        self.maplist=list(
            map(lambda x:transfer_table_dict[x],self.counter_list)            
            )
        self.maplist.reverse()#for output format.
        self.output=reduce(lambda x,y:x+y,self.maplist)
        return self.output
        
        
def short_urlto_long(url,_headers_=headers):
    temp302=requests.get(url,headers=_headers_,
            allow_redirects=False,
            timeout=1)
    if(temp302.status_code>=300 and temp302.status_code<=305):
        temp302_result=temp302.content.decode()
        #return temp302_result
        get_long_url=url_pattern.findall(temp302_result)
        return get_long_url
    else:
        logging.warning('Url:%s not redirectable'%url)
        raise ValueError(url,temp302.status_code)
def get_long_url(genurl_obect,num):
    res=[]
    for i in range(num):
        try:
            hosturl=sina_shorturl+genurl_obect.get_next()
            geturl=short_urlto_long(hosturl)
            res.append(geturl[0])
        except ValueError as e:
            logging.info(e)
        except IndexError as e:
            logging.info(e)
    return res
if __name__=='__main__':
    #url fetch test    
    get=short_urlto_long(test_url)
    maplist=list('RqC4kZg')
    print(get[0])
    
    #url gen test
    Gen_test=Gen_url()
    print(Gen_test.get_next())
    