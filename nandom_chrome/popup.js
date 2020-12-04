let randomNetflix = document.getElementById("randomNetflix");

randomNetflix.onclick = function(element) {
    fetch('https://nandom.ew.r.appspot.com').then(r => r.text()).then(result => {
        document.write(result);
    });
};

/*chrome.webRequest.onBeforeRequest.addListener(() => {

})*/