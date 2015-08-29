// ==UserScript==
// @name         JwinfoAutomationLogin
// @namespace    https://github.com/6769/m14kabing
// @version      0.4
// @description  automatic login.
// @author       pypi
// @match        http://10.202.78.11/default2.aspx
// @match        http://jwbinfosys.zju.edu.cn/default2.aspx
// @grant        none
// ==/UserScript==
'use strict';
var StudentID="0000000000";//Your StudentsID;

var PassworD="0000000000";//Your password of the website;


var StudentBox="TextBox1";
var PassworDBox="TextBox2";
var VerifyCodeBox="Textbox3";//what a fuck....TextBox in the front,Textbox here....
var ErrorCode="0";
var RegularExpress="\\d{5}";

var Debug=1;//1 ===Debug;0===release;
var StringOfImage;
var Host="http://localhost:8000/polls/api";


//environment initialized;
function DebugSwitch(booleanvalue){
    if(!booleanvalue){
        console.log=function(){
            //pass
        };
    }
}
function inputVerifyCode (number) {
    var number_confirm=new RegExp(RegularExpress);
    var number_int;
    if (number.length===5 && typeof(number)==='string') 
        if(number=number.match(number_confirm)){
            //regular express;
            number_int=parseInt(number);
            document.getElementById(VerifyCodeBox).value=number;
        }
    else{
        document.getElementById(VerifyCodeBox).value=ErrorCode;
    }
    else{
        document.getElementById(VerifyCodeBox).value=ErrorCode;
    }






}

//use VerifyCodeImage;
function getBase64Image(img) {
    // Create an empty canvas element
    var canvas = document.createElement("canvas");
    // canvas.width = img.width-5;//60*22,actually 65*24
    // canvas.height = img.height-2;
    canvas.width =60;
    canvas.height =22;
    // Copy the image contents to the canvas
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    // Get the data-URL formatted image
    // Firefox supports PNG and JPEG. You could check img.src to
    // guess the original format, but be aware the using "image/jpg"
    // will re-encode the image.
    var dataURL = canvas.toDataURL("image/png");


    //debugtest
    console.log(dataURL);
    window.open(dataURL);

    //during most periods,Base64code presents well ,Howerver,B64String length become very short,
    //It's happens 5/20;
    return dataURL.replace("data:image/png;base64,",'');
}

function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
        {
            console.log(xmlHttp.responseText);
            callback(xmlHttp.responseText);}
    }
    console.log(theUrl);
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}



function maintask ( ) {
    var b64string;
    DebugSwitch(Debug);

    //convertImage->string
    img=document.getElementsByTagName('img')[0];
    b64string=getBase64Image(img);



    //
    StringOfImage=Host+"?img="+b64string;


    httpGetAsync(StringOfImage,inputVerifyCode);

    document.getElementById(StudentBox).value=StudentID;
    document.getElementById(PassworDBox).value=PassworD;	

}

maintask();