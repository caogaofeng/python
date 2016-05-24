#coding=utf-8
import urllib
import re
import sql
import time
import random
import login_page
import sys
import urllib2


first_url = 'http://www.douban.com/people/shoy1011/statuses'
ms = sql.MSSQL(host="127.0.0.1",user="sa",pwd="123456",db="spider")
type = sys.getfilesystemencoding()
r = login_page.login_page().login(first_url)
print 'wai mian:'+r.url

if r.url == first_url:
    wrong_people = r.url.split('/')[4]
    print 'Login successfully!!!'
    #content = urllib2.urlopen(r.url).read()
    # 转换编码
    #content = content.decode("UTF-8").encode(type)
    #print r.encoding
    content = r.text.encode(type)
    match_respond_href = re.findall(r'<a\s+href="(.*?)"\s+class="btn btn-action-reply"\s+data-action-type="showComments">(.*?)<\/a>',content)
    #match_respond_href = re.findall(r'<span\s+class="count like-count"(.*?)<\/span>',content)
    #print content
    status_id = []
    statuser = []
    true_statuser = []
    respond_href = []
    respond_num = []
    temp = 0
   
    #print len(match_respond_href)
    for i in range(0,len(match_respond_href)):
        #print true_statuser
        #有回应的广播连接才再次读取
        #print len(list(match_respond_href[i])[1].encode('utf-8'))
        print len(list(match_respond_href[i])[1])
        if(len(list(match_respond_href[i])[1]) > 4):#有回应的广播的信息才爬下来
            #广播ID
            status_id.append(list(match_respond_href[i])[0].split('/')[6])
            #print status_id[i]
            #真实广播发布者
            true_statuser.append(list(match_respond_href[i])[0].split('/')[4])
            respond_href.append(list(match_respond_href[i])[0])
            #temp = i
    r.close()

    for i in range(0,len(respond_href)):
        temp = i
        commenter_id = []
        commenter_name = []
        comment_time = []
        #print respond_href[i]
        r = login_page.login_page().login(respond_href[i])
        if r.url == respond_href[i]:
            #content = urllib2.urlopen(respond_href[i]).read()
            #评论时间
            #comment_time = re.findall(r'<span\s+class="created_at">(.*?)<\/span>',content)
           
            content1 = r.text.encode(type)
            commenter = re.findall(r'<span\s+class="created_at">(.*?)<\/span>.*?<a\s+href="http:\/\/www\.douban\.com\/people\/(.*?)<\/a>',content1,re.S)
            #print commenter
            print "评论人数:"+str(len(commenter))
            #评论内容
            match_commets = re.findall(r'<p\s+class="text">(.*?)<\/p>',content1,re.S)
            print "评论条数:"+str(len(match_commets))
            for i in range(0,len(commenter)):
                commenter_id.append(list(commenter[i])[1].split('/">')[0])
                commenter_name.append(list(commenter[i])[1].split('/">')[1])
                comment_time.append(list(commenter[i])[0])
            f = open('./statues.txt', 'a')
            for j in range(0,len(match_commets)):
                try:
                    insertSql = "insert into statuses(statuses_id,statuseser,true_statuseser,commenter_id,commenter,comment_time,comments,comments_len) values('"+\
                                    status_id[temp].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                    wrong_people.decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                    true_statuser[temp].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                    commenter_id[j].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                    commenter_name[j].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                    comment_time[j].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                    match_commets[j].decode(type).encode('UTF-8').replace("'","''")+"','"+\
                                    str(len(match_commets[j].decode(type).encode('UTF-8').replace("'","''")))+\
                                    "')"
                    ms.ExecNonQuery(insertSql)
                except Exception as err:
                    print err
                    f.write(status_id[temp])
                    f.write('\n')
            f.close()
            r.close()
        else:
            print "failed!"
    print "插入完成！"
else:
    print "failed!"