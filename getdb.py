from mitmproxy import http
import json
import logging
import string
from urllib.parse import urlsplit

logging.basicConfig(filename='film_database',
                    filemode='w',
                    level=logging.INFO,
                    format='%(message)s')



def request(flow: http.HTTPFlow):
    if "netflix.com/nq/website/memberapi" in flow.request.pretty_url:
        if hasattr(flow.request.data, 'content'):
            content = flow.request.data.content
           # logging.info(content)
            content = content.decode('utf-8')
            index = content.find("videos")
            if index >= 0:
                index2 = 0
                while content[index2 + 3] != '%':
                    index = content.find("%2C", index)
                    while content[index + 3] == '%':
                        index += 3
                    index2 = content.find("%", index + 3)
                    #logging.info(content)
                    logging.info(content[index + 3:index2])
                    #logging.info(content[index2 + 3])
                    index = index2
           # for (i = 0, i < len(content), i++):


