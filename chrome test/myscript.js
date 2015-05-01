//document.body.style.backgroundColor = "blue";
var p = document.body.getElementsByTagName("p");
for (var i=0; i< p.length;i++){
    //if (i % 2 == 0 ){
	p[i].style.color = "yellow";
	p[i].style.backgroundColor = "gray";
	p[i].innerHTML = "<marquee>ALL YOUR BASE ARE BELONG TO US</marquee!";
   // }
}
