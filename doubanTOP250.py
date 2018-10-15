# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:55:27 2018

@author: 10923
"""

import urllib
import time
from bs4 import BeautifulSoup

class DoubanMovie:
    """
该类含有5个属性，姓名，连接，描述，排名,评分
"""
    def __init__(self,name,url,dec,rank,grade):
        self.name=name
        self.url=url
        self.dec=dec
        self.rank=rank
        self.grade=grade
    def output(self):
        print(self.rank+' '+self.grade+' '+self.name+'\n'+
              self.url+'\n'+self.dec+'\n')
    def write(self,filename):
        filename.write((self.rank+' '+self.grade+' '+self.name+'\n'+
              self.url+'\n'+self.dec+'\n'))

def main():
    url='https://movie.douban.com/top250?start='
    movies=[]
    for i in range(10):
        urltemp=url+str(i*25)+'&filter='
        data=urllib.request.urlopen(urltemp).read().decode('utf-8')
        parse=BeautifulSoup(data,'html.parser')
        items=parse.find_all('div',{'class':'info'})
        print(i)
        for k in range(len(items)):
            names=items[k].find_all('span',{'class':'title'})
            name=''
            for j in names:
                name+=j.get_text().strip()
            urlmovie=items[k].find('a',{'class':''}).get('href').strip()
            try:
                dec=items[k].find('p',{'class':'quote'}).get_text().strip()
            except:
                dec=''
            rank=str(i*25+k+1)
            grade=items[k].find('span',{'class':'rating_num'}).get_text().strip()
            movie=DoubanMovie(name,urlmovie,dec,rank,grade)
            movies.append(movie)
            
    for  movie in movies:
        movie.output()
    with open ('豆瓣top250.txt','w',encoding='utf-8') as f:
        for movie in movies:
            movie.write(f)

if __name__=='__main__':
    main()
