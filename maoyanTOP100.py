# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 12:42:28 2018

@author: 10923
"""

import requests
from requests.exceptions import RequestException
import re

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

def get_one_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    print(items)
    return items

    
def write_to_file(content):
        with open('result3.txt','a') as f:
            try:
                f.write(str(content))
            except:
                pass
    
def main(offset):
    url='http://maoyan.com/board/4?offset=' + str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
    
if __name__=='__main__':
    for i in range(10):
        main(i*10)
