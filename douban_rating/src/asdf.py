# -*- coding:utf-8 -*-
'''
Created on 2015年9月19日

@author: Administrator
'''

import urllib
import urllib2
import re
 
 
url = 'http://www.douban.com/subject/26309909/?dcs=index-hot'
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print "获取页面成功"
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
content = response.read().decode('utf-8')
pattern = re.compile('<span\s+class="pubtime">.*?</span(.*?)</div>',re.S)
items = re.findall(pattern,content)
print items
list = []
for item in items:
    if item.count("title") == 0:
        list.append("")
    if item.count("力荐"):
        list.append("5")
    elif item.count("推荐"):
        list.append("4")
    elif item.count("还行"):
        list.append("3")
    elif item.count("很差"):
        list.append("2")
    print list