// ==UserScript==
// @name         Jwinfo View courses's info
// @namespace    http://blog.5pipi.tk/
// @version      0.3
// @description  enter something useful
// @author       pypi
// @match        http://jwbinfosys.zju.edu.cn/xskbcx.aspx*
// @grant        none
// @updateURL    https://github.com/6769/m14kabing/raw/master/jwinfoCourseLinkReplace.js
// @downloadURL  https://github.com/6769/m14kabing/raw/master/jwinfoCourseLinkReplace.js
// ==/UserScript==

//running test
//alert(10086);
//eg  http://jwbinfosys.zju.edu.cn/html_kc/031E0031.html
var Course_Info_Header="http://jwbinfosys.zju.edu.cn/html_kc/";

function ReplaceID(atag,stringtoreplace_header){
    atag.onclick=function(){};
    atag.href=stringtoreplace_header+atag.textContent+".html";
    console.log(atag.href);
}

function SolveTable(){
	var point;
	all_A_tag=document.getElementsByTagName('a');
	for (var i = 0  ; i<all_A_tag.length; i=i+3) {
		point=all_A_tag[i];
		ReplaceID(point,Course_Info_Header);
	};

}
SolveTable();