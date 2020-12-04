chrome.runtime.onInstalled.addListener(function() {
});  

chrome.browserAction.onClicked.addListener(function(activeTab){
    fetch('https://nandom.ew.r.appspot.com').then(r => r.text()).then(result => {
        newURL = result;
        chrome.tabs.create({ url: newURL });
    });
  });