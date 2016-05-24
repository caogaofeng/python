# -*- coding:utf-8 -*-
import urllib
import urllib2
import re  
page = 1
url = 'http://www.douban.com/subject/11472102/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
try:    
    request = urllib2.Request(url,headers = headers)    
    response = urllib2.urlopen(request)               
    content = response.read().decode('utf-8')  
    #pattern = re.compile('<div class="user-info".*?<a.*?href="http:\/\/www\.douban\.com/people\/(.*?)/">(.*?)</a>.*?<span class="allstar50" title="(.*?)"></span>.*?<p>(.*?)</p>',re.S)
    pattern = re.compile('<div class="user-info">.*?<a href="(.*?)/">.*?</a>',re.S)
    items = re.findall(pattern,content)
    list_id = []
    for i in range(0,len(items)): 
        list_id.append(items[i].split('people/')[1])
        print list_id
    pattern1 = re.compile('<div class="user-info">.*?<a href=".*?">(.*?)</a>.*?'+
                          '<span class="pubtime">.*?title="(.*?)".*?</div>.*?<p>(.*?)</p>',re.S)
    items1 = re.findall(pattern1,content)
    print items1[0].encode("utf-8"),items1[1].encode("utf-8"),items1[2].encode("utf-8")
    

    
except urllib2.URLError, e:   
             if hasattr(e, "code"):        
                print e.code   
             if hasattr(e, "reason"):        
                print e.reason