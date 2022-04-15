# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:15:51 2022

@author: user
"""
import urllib
import requests
from  bs4 import BeautifulSoup
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
my_params={'q':'寒流'}
#data = requests.get('https://www.google.com/search?q=%E5%AF%92%E6%B5%81',headers= my_headers)
data = requests.get('https://www.google.com/search',headers= my_headers,params=my_params)
if data.status_code==200:
     soup = BeautifulSoup(data.text,'html.parser')
     # print(soup)
     items=soup.select('div.v7W49e  h3')
     itemslink=soup.select('div.v7W49e a')
     for t,l in zip(items,itemslink):
         print('標題: ',t.text.strip())
         print('網址: '+urllib.parse.unquote(l.get('href'))) 
         #urllib.parse.unquote 將中文網址轉成中文
         
     
     
         
         