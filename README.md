# Nandom

Nandom is a chrome extension to watch a random Netflix Movie

## Introduction

This extension isn't available yet on the Chrome Store but you can install it manually. More about that later.

## Prerequisites

If you want to change the code, you'll need at least python 3.8.6, mitmproxy and pip.
If you just want the extension to work, be connected to your Netflix account on Google Chrome.

### Setup for developers

Clone the repo:
```
git clone https://github.com/msiesse/Nandom.git
```

Install mitmproxy:
```
pip install mitmproxy
```

Configure the proxy for HTTP/HTTPS on localhost and port 8080.

If you want to use the web scrapper you'll have to create a credentials file with your Netflix infos:
```
emailaddress
password
profileId
```

profileId follows the order of profiles from left to right when you have to select one.
If the profile "John" is the third on the list, profileId = 2

Now you can launch manually python scripts.
```
> mitmdump -s getdb.py (to read requests and store movies Ids)
> python scrap.py (to launch the web scrapper)
> python sort_database.py (to get unique IDs movies)
> python select_random.py (to open a random movie on Chrome)
```

### Setup for Users

Clone the repo:
```
git clone https://github.com/msiesse/Nandom.git
```

On Chrome, go to chrome://extensions and enable Developer Mode then click on "Load unpacked" and select the nandom_chrome folder.

Refresh if you don't see the extension. Now you can pin it and use it directly on Chrome

## Notes on the Server

You can implement your own version of the extension with your server. You'll have to change manifest.json and background.js on the extension folder to work with your server.
The nandom_server folder is designed to work with google cloud services. If you want to use AWS or other services, you'll have to make some changes.
