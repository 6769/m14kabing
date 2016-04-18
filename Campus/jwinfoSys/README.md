5pip's  Script Repertory 
=========================

.
##1. JwinfoLogin.js##

this script needs an API as verify code transformer. An availlable one for our test is [http://api.5pipi.tk/api/zjuocr?img=<base64encoded img>](http://api.5pipi.tk/api/zjuocr?img=<base64encoded img> "http://api.5pipi.tk/api/zjuocr?img=<base64encoded img>").This script work for this flow:

1. Load the original page,
2. Get image object and describe in Base64 form.
3. In xmlhttp,send out previous base64 encoded strings and API will return the number.
4. Fill it!

##2. JwinfoCourseLinkReplace.js ##

This will be easy in page use http://jwbinfosys.zju.edu.cn/xskbcx.aspx?xh=313010xxxx; 
however,some problems haven't solved in table and list modes.