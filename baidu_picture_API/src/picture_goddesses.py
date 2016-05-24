# -*- coding: utf-8 -*-

import sys, urllib, urllib2, json
import requests

# 官网示例
url = 'http://apis.baidu.com/dajuncloud/goddess/goddesses?tuid=7'

apikey = "d7b1091b8aadb18ed19f9001370bc1d9"
#apikey = "698cb4351b5c3c12de177b7e2d5f051d"

req = urllib2.Request(url)
req.add_header("apikey", apikey)
resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)

url_1 = 'http://apis.baidu.com/dajuncloud/goddess/goddesses'
apikey = "698cb4351b5c3c12de177b7e2d5f051d"
headers = {'apikey':apikey}
params = {'tuid':'4'}

# 发出请求，得到响应
r = requests.get(url_1, params = params,headers = headers)
print r
resp = urllib2.urlopen(req)
contents = resp.read()
content_dict = eval(contents)
print content_dict

# 定义一个存图片的函数
def saveImage(imgUrl, imgName= 'default.jpg'):
    response = requests.get(imgUrl, stream = True)
    image = response.content
    dst = "f:/baidu_picture/picture_goddesses/"
    path = dst + imgName
    print 'save the file:' + path + '\n'
    with open(path,'wb') as img:
        img.write(image)
    img.close()

# 获取图片地址，保存       
def run():
    imgName = content_dict['tu_name']
    picUrl = content_dict['tu_dizhi']
    saveImage(picUrl, imgName = imgName + '.jpg')
        
run()