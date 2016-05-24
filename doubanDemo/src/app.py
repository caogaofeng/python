# coding=utf-8
import urllib2
import re
import sys
import sql
import time
import random

# reload(sys)
# sys.setdefaultencoding("utf-8")
# 获取当前系统编码格式
type = sys.getfilesystemencoding()
j = 0
type_id = [1083,1053,1067,1063,1068,1086,1054,1058,1072,1079,1065,1089,1087]
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
    content = content.decode("UTF-8").encode(type)
    # 读取应用名称
    list_name = []
    list_href = []
    list_class_name = []
    list_class_id = []
    # 读取应用ID
    match_id = re.findall(r'<a\s+class="name"\s+href="http\:\/\/www\.douban\.com\/subject\/([0-9.]+)\/\?dcs=index-hot">', content)
    # 读取分数
    match_scol = re.findall(r'<span\s+class="rating_nums">([0-9.]+)<\/span>', content)
    # 读取分类
    match_class = re.findall(r'<a\s+href="\/app\/android\?cat_id=(.*?)<\/a>', content)
    for i in range(0,len(match_class)):
        # 读取分类名字
        list_class_name.append(match_class[i].split('">')[1]) 
        # 读取分类ID
        list_class_id.append(match_class[i].split('">')[0])
    match_name = re.findall(r'<a\s+class="name"\s+href="(.*?)<\/a>', content)
    for i in range(0,len(match_name)):
        list_name.append(match_name[i].split('">')[1]) 
        list_href.append(match_name[i].split('">')[0])
    match_intro=[]
    for i in range(0,len(list_href)):
        time.sleep(int(random.uniform(1, 1)))
        content1 = urllib2.urlopen(list_href[i]).read()
        content1 = content1.decode("UTF-8").encode(type)
        string = re.findall(r'<p>(.*?)<\/p>', content1)[0]
        if "<br />" in string:
            #读取简介
            match_intro.append(string.replace("<br/>",""))
    # 压缩到一个列表
    zipc = zip(list_name, match_scol, match_intro,list_class_name,match_id,list_class_id)
    # 打开文档
    f = open('./app.txt', 'a')
    # 写入文件
    try:
        for name in zipc:
            #编码没问题直接存入数据库
            insertSql = "insert into apps(name,score,intro,class,app_id,class_id) values('"+\
                        name[0].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                        name[1].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                        name[2].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")[0:3500]+"','"+\
                        name[3].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                        name[4].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+"','"+\
                        name[5].decode(type,'ignore').encode("UTF-8",'ignore').replace("'","''")+\
                        "')"
            ms.ExecNonQuery(insertSql) 
    except Exception as err:
        #编码有问题的记录暂时存入txt文件
        print err 
        f.write(name[0])
        f.write('\t')
        f.write(name[1])
        f.write('\t')
        f.write(name[2])
        f.write('\t')
        f.write(name[3])
        f.write('\t')
        f.write(name[4])
        f.write('\t')
        f.write(name[5])
        f.write('\n')               
print 'done'
f.close()    