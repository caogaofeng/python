# -*- coding: utf-8 -*-

import sys, urllib, urllib2, json
import requests

# 官网示例
url = 'http://apis.baidu.com/txapi/mvtp/meinv?num=10'
apikey = "698cb4351b5c3c12de177b7e2d5f051d"
req = urllib2.Request(url)
req.add_header("apikey", apikey)
resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)

     
   
url = 'http://apis.baidu.com/txapi/mvtp/meinv'
apikey = "698cb4351b5c3c12de177b7e2d5f051d"
headers = {'apikey':apikey}
params = {'num':'10'}

# 发出请求，得到响应
r = requests.get(url, params = params, headers=headers)
print r
r = r.json()
print r

# 定义一个存图片的函数
def saveImage(imgUrl,imgName= 'default.jpg'):
    response = requests.get(imgUrl,stream = True)
    image = response.content
    dst = "f:/baidu_picture/baidu_img"
    path = dst + imgName
    print 'save the file:' + path + '\n'
    with open(path,'wb') as img:
        img.write(image)
    img.close()

# 获取图片地址，保存       
def run():
    for line in r['newslist']:
        title = line['title']
        picUrl = line['picUrl']
        saveImage(picUrl,imgName=title+'.jpg')
        
run()