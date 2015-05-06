/*var jq = document.createElement('script');
jq.src = "//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js";
document.querySelector('head').appendChild(jq);

jq.onload = procede;

/


function procede () {*/
/*
console.log("hello");
var CSSContent ="<style>#panel {width: 200px;height: 600px;position: absolute;top: -400px;left: 500px;z-index: 200;background-color: #333333;}#panel-tab {width: 140px;height: 40px;position: absolute;bottom: -40px;right: 0px;    background-color: #000000;    text-decoration: none;color: #FFFFFF;}}#panel-tab {width: 140px;height: 40px;position: absolute;bottom: -40px;right: 0px;background-color: #000000;text-decoration: none;color: #FFFFFF;}#panel-tab:focus {outline: none;}</style>";


var head = document.getElementsByTagName("head")[0];

head.innerHTML+='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />';
//head.innerHTML+='<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>';
head.innerHTML+=CSSContent;



var content = document.createElement("div");
content.innerHTML ='<div id="panel"><a href="#" id="panel-tab">Click Me</a><p>Panel content goes here</p></div>'
    document.body.appendChild(content);
document.body.innerHTML+='<script type = "text/javascript"> console.log("down");var sipPos = 0; $("document").ready(function() {$("#panel-tab").click(function(e) {e.preventDefault();$("#panel").animate({ top: sipPos }, 800, "linear", function() {if(sipPos == 0) { sipPos = -400; }else { sipPos = 0; }});});});</script>';
//}
*/
var sliderIntervalId = 0;
var sliderHeight = 232;
var sliding = false;
var slideSpeed = 10;

document.body.innerHTML+= '<script>function Slide(){if(sliding)return;sliding = true;if(sliderHeight == 232)sliderIntervalId = setInterval("SlideUpRun()", 30);elsesliderIntervalId = setInterval("SlideDownRun()", 30);}function SlideUpRun(){slider = document.getElementById("exampleSlider");if(sliderHeight <= 0){sliding = false;sliderHeight = 0;slider.style.height = "0px";clearInterval(sliderIntervalId);}else{sliderHeight -= slideSpeed;if(sliderHeight < 0)sliderHeight = 0;slider.style.height = sliderHeight + "px";}}function SlideDownRun(){slider = document.getElementById("exampleSlider");if(sliderHeight >= 232){sliding = false;sliderHeight = 232;slider.style.height = "232px";clearInterval(sliderIntervalId);}else{sliderHeight += slideSpeed;if(sliderHeight > 232)sliderHeight = 232;slider.style.height = sliderHeight + "px";}}</script>'

function Slide(){if(sliding)return;sliding = true;if(sliderHeight == 232)sliderIntervalId = setInterval("SlideUpRun()", 30);elsesliderIntervalId = setInterval("SlideDownRun()", 30);}function SlideUpRun(){slider = document.getElementById("exampleSlider");if(sliderHeight <= 0){sliding = false;sliderHeight = 0;slider.style.height = "0px";clearInterval(sliderIntervalId);}else{sliderHeight -= slideSpeed;if(sliderHeight < 0)sliderHeight = 0;slider.style.height = sliderHeight + "px";}}function SlideDownRun(){slider = document.getElementById("exampleSlider");if(sliderHeight >= 232){sliding = false;sliderHeight = 232;slider.style.height = "232px";clearInterval(sliderIntervalId);}else{sliderHeight += slideSpeed;if(sliderHeight > 232)sliderHeight = 232;slider.style.height = sliderHeight + "px";}}