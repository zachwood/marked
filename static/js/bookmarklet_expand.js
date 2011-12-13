javascript: (function () {
    var a = 'setAttribute';
    var d = document;

    function o() {
        var s2;
        if (this.readyState === 4) {
            s2 = d.createElement('script');
            s2[a]('type', 'text/javascript');
            s2.appendChild(d.createTextNode(this.responseText));
            d.body.appendChild(s2);
        }
    }
    var s = d.createElement('script');
    s[a]('type', 'text/javascript');
    //s[a]('src', 'http://marked.goodnightstudio.com/static/js/bookmarklet.js');
    s[a]('src', 'http://localhost:8000/static/js/bookmarklet.js');
    d.body.appendChild(s);
    //var x = new XMLHttpRequest();
    //x.onreadystatechange = o;
    //x.open('GET', 'http://localhost:8000/static/js/bookmarklet.js', true);
    //x.send('');
})();
