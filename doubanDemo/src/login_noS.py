#coding=utf-8
import urllib
import re
import sql
import time
import random
import login_page_noS
import sys
import urllib2
from matplotlib.cbook import ls_mapper


ms = sql.MSSQL(host="127.0.0.1",user="sa",pwd="123456",db="spider")
type = sys.getfilesystemencoding()
url_list = ms.ExecQuery('select distinct(comment_id) from usercomments')
s= login_page_noS.login_page().login()
print url_list
for i in range(0,len(url_list)):
    first_url = 'http://www.douban.com/people/'+list(url_list[i])[0].strip()+'/statuses'
    print first_url
    time.sleep(int(random.uniform(1, 3)))
    try:
        r = s.get(first_url)
    except Exception as err:
        time.sleep(int(random.uniform(60, 60)))#连接错误，等一分钟继续跑
        continue;
    print 'wai mian:'+r.url
    if r.url==first_url:
        wrong_people = r.url.split('/')[4]
        #print 'Login successfully!!!'
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
        for i in range(0,len(match_respond_href)):
            #print true_statuser
            #有回应的广播连接才再次读取
            #print len(list(match_respond_href[i])[1].encode('utf-8'))
            #print len(list(match_respond_href[i])[1])
            if(len(list(match_respond_href[i])[1]) > 4):#有回应的广播的信息才爬下来
                #广播ID
                if 'www.douban.com' in list(match_respond_href[i])[0]:
                    status_id.append(list(match_respond_href[i])[0].split('/')[6])
                    print "广播ID:"+status_id[len(status_id)-1]
                    #真实广播发布者
                    true_statuser.append(list(match_respond_href[i])[0].split('/')[4])
                    respond_href.append(list(match_respond_href[i])[0])
                if 'site.douban.com' in list(match_respond_href[i])[0]:
                    status_id.append(list(match_respond_href[i])[0].split('/')[5])
                    print "广播ID:"+status_id[len(status_id)-1]
                    #真实广播发布者
                    true_statuser.append(list(match_respond_href[i])[0].split('/')[3])
                    respond_href.append(list(match_respond_href[i])[0])
                #temp = i
        #r.close()
        for i in range(0,len(respond_href)):
            temp = i
            commenter_id = []
            commenter_name = []
            comment_time = []
            comments = []
            #print respond_href[i]
            time.sleep(int(random.uniform(1, 3)))
            try:
                r = s.get(respond_href[i])
            except Exception as err:
                time.sleep(int(random.uniform(60, 60)))#连接错误，等一分钟继续跑
                continue;
            if r.url == respond_href[i]:
                #content = urllib2.urlopen(respond_href[i]).read()
                #评论时间
                #comment_time = re.findall(r'<span\s+class="created_at">(.*?)<\/span>',content)
                print r.url
                content1 = r.text.encode(type)
                #包括时间，评论人，评论内容
                commenter = re.findall(r'<span\s+class="created_at">(.*?)<\/span>.*?<a\s+href="http:\/\/www\.douban\.com\/people\/(.*?)<\/a>.*?p\s+class="text">(.*?)<\/p>',content1,re.S)
                #print commenter
                print "评论人数:"+str(len(commenter))
                #评论内容
                #match_commets = re.findall(r'<p\s+class="text">(.*?)<\/p>',content1,re.S)
                #print "评论条数:"+str(len(match_commets))
                for i in range(0,len(commenter)):
                    commenter_id.append(list(commenter[i])[1].split('/">')[0])
                    commenter_name.append(list(commenter[i])[1].split('/">')[1])
                    comment_time.append(list(commenter[i])[0])
                    comments.append(list(commenter[i])[2])
                f = open('./statues.txt', 'a')
                for j in range(0,len(commenter)):
                    try:
                        insertSql = "insert into statuses_bak(statuses_id,statuseser,true_statuseser,commenter_id,commenter,comment_time,comments,comments_len) values('"+\
                                        status_id[temp].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                        wrong_people.decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                        true_statuser[temp].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                        commenter_id[j].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                        commenter_name[j].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                        comment_time[j].decode(type).encode("UTF-8").replace("'","''")+"','"+\
                                        comments[j].decode(type).encode('UTF-8').replace("'","''")+"','"+\
                                        str(len(comments[j].decode(type).encode('UTF-8').replace("'","''")))+\
                                        "')"
                        ms.ExecNonQuery(insertSql)
                    except Exception as err:
                        print err
                        f.write(status_id[temp])
                        f.write('\n')
                f.close()
                #r.close()
            else:
                print "failed!"
    else:
        print "failed!"
print "Done!"