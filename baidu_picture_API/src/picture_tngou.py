# -*- coding: utf-8 -*-

import requests

# 天狗网
url_1 = "http://www.tngou.net/tnfs/api/list?page=2"
url_2 = "http://www.tngou.net/tnfs/api/classify"
src_header = "http://tnfs.tngou.net/image"


r = requests.get(url_1)
r = r.json()
print r


# 保存图片到本地路径
def saveImage(imgUrl, imgName= 'default.jpg'):
    response = requests.get(imgUrl, stream = True)
    image = response.content
    dst = "f:/baidu_picture/picture_tiangou/"
    path = dst + imgName
    print 'save the file:' + path + '\n'
    with open(path,'wb') as img:
        img.write(image)
    img.close()
    
# 开始
def run():
    for line in r['tngou']:
        title = line['title']
        img = line['img']
        src_path = src_header + img
        saveImage(src_path, title + '.jpg')
run()