# -*- coding: utf-8 -*-

import argparse 
import re 
from multiprocessing import Pool  # 用来创建子进程
import requests # 加载网页
import bs4      # 解析HTML
import time 
import json 
import io  

root_url = 'http://wufazhuce.com' 
 
def get_url(num):     
    return root_url + '/one/' + str(num)  

def get_urls(num):     
    urls = map(get_url, 
    range(100,100+num))     
    return urls  

def get_data(url):   
    dataList = {}   
    response = requests.get(url)   
    if response.status_code != 200:       
        return {'noValue': 'noValue'}   
    soup = bs4.BeautifulSoup(response.text,"html.parser")   
    dataList["index"] = soup.title.string[4:7]   
    for meta in soup.select('meta'):     
        if meta.get('name') == 'description':       
            dataList["content"] = meta.get('content')   
            dataList["imgUrl"] = soup.find_all('img')[1]['src']   
    return dataList  

if __name__=='__main__':   
    pool = Pool(4)   # pool 用来创建子进程  
    dataList = []   
    urls = get_urls(10)  
    start = time.time()   
    dataList = pool.map(get_data, urls)   
    end = time.time()  
    print 'use: %.2f s' % (end - start)   
    jsonData = json.dumps({'data':dataList}) # json.dumps 将字典转换为json格式  
    with open('data.txt', 'w') as outfile:     
        json.dump(jsonData, outfile)
