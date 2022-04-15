# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:03:26 2022

@author: user
"""
import re
import pandas as pd
import requests
from  bs4 import BeautifulSoup
titles,urls,times=[],[],[]
search=['big-data','cloud','devops']
print('Ai')
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
for i in range(3):
    data = requests.get('https://www.ithome.com.tw/big-data?page='+str(i),headers= my_headers)
    if data.status_code==200:
        soup = BeautifulSoup(data.text,'html.parser')
        #print(soup)  確定有抓到資料
        title= soup.find('div',class_=re.compile('view view-featured-channel view-id-featured_channel view-display-id-views_fc_big_data view-dom-id-*')).find_all('p',class_='title')
        # for t in title: 
        #     print(t.text) #找到標題
        #     print('https://www.ithome.com.tw'+t.a.get('href')) #跟標題網址
        time =soup.find('div',class_=re.compile('view view-featured-channel view-id-featured_channel view-display-id-views_fc_big_data view-dom-id-*')).find_all('p',class_='post-at')
        # for l in time:
        #     print(l.text)
        for t,ti in zip(title,time):
            titles.append(t.text.strip()) #找到標題
            urls.append('https://www.ithome.com.tw'+t.a.get('href'))
            times.append(ti.text.strip())
print('cloud')
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
for i in range(3):
    data = requests.get('https://www.ithome.com.tw/cloud?page='+str(i),headers= my_headers)
    if data.status_code==200:
        soup = BeautifulSoup(data.text,'html.parser')
        #print(soup)  確定有抓到資料
        title= soup.find('div',class_=re.compile('view view-featured-channel view-id-featured_channel view-display-id-views_fc_cloud view-dom-id-*')).find_all('p',class_='title')
        # for t in title: 
        #     print(t.text) #找到標題
        #     print('https://www.ithome.com.tw'+t.a.get('href')) #跟標題網址
        time =soup.find('div',class_=re.compile('view view-featured-channel view-id-featured_channel view-display-id-views_fc_cloud view-dom-id-*')).find_all('p',class_='post-at')
        # for l in time:
        #     print(l.text)
        for t,ti in zip(title,time):
            titles.append(t.text) #找到標題
            urls.append('https://www.ithome.com.tw'+t.a.get('href'))
            times.append(ti.text)
            
print('devops')
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
for i in range(3):
    data = requests.get('https://www.ithome.com.tw/devops?page='+str(i),headers= my_headers)
    if data.status_code==200:
        soup = BeautifulSoup(data.text,'html.parser')
        #print(soup)  確定有抓到資料
        title= soup.find('div',class_=re.compile('view view-view-news view-id-view_news view-display-id-page_2 view-dom-id-*')).find_all('p',class_='title')
        # for t in title: 
        #     print(t.text) #找到標題
        #     print('https://www.ithome.com.tw'+t.a.get('href')) #跟標題網址
        time =soup.find('div',class_=re.compile('view view-view-news view-id-view_news view-display-id-page_2 view-dom-id-*')).find_all('p',class_='post-at')
        # for l in time:
        #     print(l.text)
        for t,ti in zip(title,time):
            titles.append(t.text) #找到標題
            urls.append('https://www.ithome.com.tw'+t.a.get('href'))
            times.append(ti.text)
            
dataframe = pd.DataFrame({'ppt_title' : titles , 'ppt_url' : urls , 'ppt_time' : times })
dataframe.to_csv("ithome.csv",index=False,sep=',',encoding='utf-8-sig',)