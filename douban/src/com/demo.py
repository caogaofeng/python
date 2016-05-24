

import urllib2
import re
import sys

#
type = sys.getfilesystemencoding()
j = 0
type_id = [1083,1053,1067,1063,1068,1086,1054,1058,1072,1079,1065,1089,1087]
for i in range(0,len(type_id)):
    url = 'http://www.douban.com/app/?platform=android'
    hash = '&cat_id=%d' % int(type_id[i])
    #hash = 'start=%d&type=T' % i
    url = url + hash  
     
    content = urllib2.urlopen(url).read()
     
    content = content.decode("UTF-8").encode(type)
   
    list_name = []
    list_href = []
    match_name = re.findall(r'<a\s+class="name"\s+href="(.*?)<\/a>', content)
    for i in range(0,len(match_name)):
        list_name.append(match_name[i].split('">')[1]) 
        list_href.append(match_name[i].split('">')[0])
    match_intro=[]
    for i in range(0,len(list_href)): 
        content1 = urllib2.urlopen(list_href[i]).read()
        content1 = content1.decode("UTF-8").encode(type) 
        if "<br />" in re.findall(r'<p>(.*?)<\/p>', content1)[0]:
            
            match_intro.append(re.findall(r'<p>(.*?)<\/p>', content1)[0].replace("<br />",""))
            print match_intro  
     
    match_scol = re.findall(r'<span\s+class="rating_nums">([0-9.]+)<\/span>', content)
    
    zipc = zip(list_name, match_scol, match_intro)
    
    f = open('./app.txt', 'a')
    
    for name in zipc:
        
        f.write(name[0])
        f.write('\t')
        f.write(name[1])
        f.write('\t')
        f.write(name[2])
        f.write('\n')          
print 'done'
f.close()