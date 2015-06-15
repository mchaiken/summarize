function popup(url) {
    var w = window.open(url, "Summarize!", "width=500, height=500");
    return w
}
//popup("http://google.com");

var url = window.location.href;

while (url.indexOf("/") != -1){
    url=url.replace("/","_9l");
    q = url.indexOf("?")
    if (q != -1){
        url=url.substring(0,q)
    }
}

var win = popup("http://127.0.0.1:5000/summary/"+url);
//win.location.href= url;
console.log(win)
//win.location.onLoad = win.location.reload();