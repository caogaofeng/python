# -*- coding:utf-8 -*-
import urllib2
import re
import sys
import sql
import time
import random
import pymssql

# reload(sys)
# sys.setdefaultencoding("utf-8")
# 获取当前系统编码格式
type = sys.getfilesystemencoding()
type_id = [1083,1053,1067,1063,1068,1086,1054,1058,1072,1079,1065,1089,1087]
temp = 0
# proxy_addr = ["http://203.100.80.81:8080","http://101.251.238.123:8080","http://106.37.177.251:3128","http://61.157.126.37:18000"]
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://183.63.149.110:3128'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
ms = sql.MSSQL(host="127.0.0.1",user="sa",pwd="123456",db="spider")
for i in range(0,len(type_id)):
    url = 'http://www.douban.com/app/?platform=android'
    hash = '&cat_id=%d' % int(type_id[i])
    #hash = 'start=%d&type=T' % i
    url = url + hash  
    # 读取url内容
    time.sleep(int(random.uniform(1, 1)))
    content = urllib2.urlopen(url).read()
    # 转换编码
    content = content.decode('utf-8').encode(type)
    # 读取应用名称
    list_href = []
    match_name = re.findall(r'<a\s+class="name"\s+href="(.*?)<\/a>', content)
    for i in range(0,len(match_name)): 
        list_href.append(match_name[i].split('">')[0])
    # 读取应用ID
    #print list_href
    
    
    
    
    match_id = re.findall(r'<a\s+class="name"\s+href="http:\/\/www\.douban\.com\/subject\/([0-9.]+)\/\?dcs=index-hot">', content)
   # print match_id
    f = open('./comments.txt', 'a')
    for i in range(0,len(list_href)):
        #print list_href[i]
        time.sleep(int(random.uniform(1, 1)))
        content1 = urllib2.urlopen(list_href[i]).read()
        content1 = content1.decode('utf-8').encode(type)
        # 读取应用评论人
        match_people = re.findall(r'<div\s+class="user-info">\n\s\s\s\s+<a\s+href="http:\/\/www\.douban\.com\/people\/(.*?)<\/a>', content1)
       # print match_people
        #print "评论人数目："+str(len(match_people))
        temp = i
        #print temp
        list_name = []
        list_acc = []
        for j in range(0,len(match_people)):
            if(match_people[j].count('/">') > 0):
                #评论人昵称
                list_name.append(match_people[j].split('/">')[1])
                #评论人帐号
                list_acc.append(match_people[j].split('/">')[0])
                #print list_name,list_acc
        #print "评论人数目："+str(len(list_name))
        string = re.findall(r'<p>(.*?)<\/p>', content1,re.S)
        #print "评论数目："+str(len(string))
        pattern = re.compile(r'<span\s+class="pubtime">.*?</span(.*?)</div>',re.S)
        items = re.findall(pattern,content1)
        #print items
        user_score = []
        for i in range(0,len(items)):
            if items[i].decode(type).encode('utf-8').count("title") == 0:
               user_score.append("")
            if items[i].decode(type).encode('utf-8').count("力荐"):
                user_score.append("5")
            elif items[i].decode(type).encode('utf-8').count("推荐"):
                user_score.append("4")
            elif items[i].decode(type).encode('utf-8').count("还行"):
                user_score.append("3")
            elif items[i].decode(type).encode('utf-8').count("很差"):
                user_score.append("2")
        #print user_score
        match_comm=[]
        for j in range(0,len(string)):
            if string[j].count("<br />") == 0 and string[j].count("加载中") == 0:
                #读取评论
                match_comm.append(string[j].replace("<br />","").lstrip())
        #print "最终评论数目："+str(len(match_comm))+"\n"
        for j in range(0,len(match_comm)):
            try:
                insertSql = "insert into usercomments(app_id,comment_user,comment_id,comments,score) values('"+\
                                match_id[temp].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                                list_name[j].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                                list_acc[j].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                                match_comm[j].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")[0:3500]+"','"+\
                                user_score[j].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+\
                                "')"
                ms.ExecNonQuery(insertSql)
            except Exception as err:
                print err
                f.write(match_id[temp])
                f.write('\n')     
print 'done'
f.close()