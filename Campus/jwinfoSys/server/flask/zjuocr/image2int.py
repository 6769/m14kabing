# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:58:13 2015

Accept a base64 encoded image,return a Image verify code.

@author: pip

@email:5pipitk@gmail.com
"""


import json
import base64
import time
import pytesseract
from PIL import Image
from io import BytesIO
try:
    from pylab import *
except ImportError:
    pass

img_size = (60, 22)



def base64strToStringIO(b64string):
    status_code=''
    im_bak=Image.new('RGB', img_size, 0)  #0 means black;
    try:
        binarystr = base64.urlsafe_b64decode(b64string)
    except :
        status_code+='-E:base64decode error-'
        return im_bak,status_code
    #    print(binarystr)
    image_vitrl_file = BytesIO(binarystr)


    try:
        im = Image.open(image_vitrl_file)
    except OSError:
        im =im_bak
        status_code += '-E:img load error-'

    print(im.size, im.mode, im.format)
    try:
        im.load()
    except IOError:
        status_code += '-E:img broken-'
        print("IOError")

    #im.show()
    #try:
    im_rgb = im.convert(mode="RGB")
    threeChannel = im_rgb.split()
    #except:

    #pass
    try:
        r, g, b = threeChannel
        
        return g,status_code
    except ValueError:
        status_code += '-W:img channel limmited -'
        number_of_channel = len(threeChannel)
        if (number_of_channel == 1):
            only_channel = threeChannel[0]
            return only_channel,status_code
        else:
            #chioce the second;
            two_channel_the_sec = threeChannel[1]
            return two_channel_the_sec,status_code


def OCR_Return_Verifycode(b64string):
    """accept string or bytes ,return str of verify code"""
    beforeRepaireStr = b64string if isinstance(b64string,bytes) else b64string.encode()
    
    #repair URL parse problem
    #last_img_str=beforeRepaireStr.replace(b' ',b'+');
    #use base64.urlsafe_decode replace
    
    last_img,status_code = base64strToStringIO(beforeRepaireStr)
    if len(status_code)>1:
        code=""
    else:
        code = pytesseract.image_to_string(last_img, lang='eng', config='-psm 7')
    print(code,status_code)
    return code,status_code


def GetVerifyCode_StatusWord(paradict):
    starttime=time.time()
    b64string=paradict.get('img')
    verifycode,statuscode = OCR_Return_Verifycode(b64string)
    endtime=time.time()
    res = dict(verify=verifycode, status=statuscode,time_cost=endtime-starttime)
    return json.dumps(res)


def main():
    png_ = """iVBORw0KGgoAAAANSUhEUgAAADwAAAAWCAYAAACcy/8iAAADgklEQVRYR+VXUbLcIAyDM8GZ4EzkTORM6QijYAiB3fZ9tNPMvNkXQoyFJZnYnPNl/qPLppSuEMIS8nmexjl3z8E9x/A7vr97/hP7exzHY91VXMwHBosKazCzl0bAmKPH8P/btYv9u+BnOb3ljnHkgXe2FV7tpK7kyADec2c1I7g4fr/ZEA1yV2GuO+a1rfCqkjpxvbuf7j6Z8g07xo0b3yXbZhu5rbC1JSUD9YK019V0zIWsPYwzzpx1HsbzFYyugLdHjSCR8pUeGL2N9zoy6zQpp84rzogs8MeMjHEpFC1rJvF+5i2PCnOHoieI/leD9pba1UlIMikLXQVsS5FgNGgB2zaN0fBeqpsTbRzANtAhp1saIyMflKZLa86zskjzqk0Lz4+IpKTSrGyuVWdFZdyYkIw5kGOtOEsqcYQ5BA3AMk8qj6SjlzguOcPKpivfzECcM8pmcnwmJY2rUHrm0gCMxVLu25G1Qm+AfHPu6AUMKhy9zE9X3/ZQ9bIp2ZnDg7yY3+bsjIwsPLwwI6iNmvkB4201PIIChVHhnMXmeck4wFGjkjzpDE3rCp+RGg21ks64ZEolSWdSeTRDgNQXNKzNkznPusZrhRlQOyI1DbC8GFSAUVPOpLohQk3ReXsqYEnfaI9us4QfMj/kBqbEcM6MWqZ+V+5MmeD3tQ9rlwWVmTQ1yyDzSouGS4IVcO+urji5sKC5c9uEeIOGhscKwn2jLdopF0DrEx/PB1+5NIM1t4ameyqPJyxxZWkdAKS1qmlIbWsNa9dG3MOLIbHKukq3PIqGjXG5b3NvHrDVsK5sSGJgpLkvhuTMOM6KapeGgWl5PDUsbsz4qIy3vsSHlkFjkUHu+i1deqxwJ3J1s9Swt1VrVbOjCYgby4XK4xKwrQ8TvDatRmNXXFrek8ML7zGmKyxGJXEBrj0XqXHsDage7zRM7scIffUnGrzEQ8NVT1LSl6XSPGlJn26uLD22tyzcU+NlTeXObdX+pKVBawDoweMZWzNFz130YQ3ieQKicYkLdyHvE5bWHDXbWk4oSZZNrDJhP2azg3bHqwctdB/deTxpMcbHX0s7mmg3J0NWOzzrk1xDv88YWvuzfrt6rl36o+/h0YV34P/m539U4Vmfe/s+ffsuXVV6t3F6/fF7e3Us3Z60dgt/+lzTjrr99N3VPM1AfV5+W+Puw99q41+e/wsQ8qnG9QcMugAAAABJRU5ErkJggg=="""
    code,status = OCR_Return_Verifycode(png_)
    print(code,status)
    
    parad=dict(img=png_)
    jsonstr=GetVerifyCode_StatusWord(parad)
    print(jsonstr)


if __name__ == "__main__":
    main()
    
