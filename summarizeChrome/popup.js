function popup(url) {
    var w = window.open(url, "Summarize!", "width=500, height=500");
    return w
}
popup("http://google.com");

var url = window.location.href;

while (url.indexOf("/") != -1){
    url=url.replace("/","%9l");
}

var win = popup("104.236.53.73/summary/"+url);
//win.location.href= url;
console.log(win)
//win.location.onLoad = win.location.reload();