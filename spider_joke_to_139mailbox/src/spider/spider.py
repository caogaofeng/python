# -*- coding:utf-8 -*-

import urllib2, json, sys, smtplib
from email.mime.text import MIMEText

reload(sys)
sys.setdefaultencoding('utf-8')  # 避免中午编码问题


mail_host = "smtp.139.com"            # 设置服务器
mail_user = " "     # 用户名
mail_pass = " "             # 密码(3254793137 qq授权码：itrdncwpuriwchai   unsrukjmhlnadbgb)
mailto_list = [' '] # 邮件接收者

def send_mail(to_list, part1, sub, content):
    # to_list: 收件人； sub: 主题； content： 邮件内容
    me = "FF发来笑话："+part1+"<"+mail_user+">"  # 发件人
    msg = MIMEText(content, _subtype='plain', _charset='utf-8') # 创建一个实例，_subtype='plain'这里设置为纯文字格式 邮件编码utf-8
    msg['Subject'] = sub            # 设置主题
    msg['From'] = me                # 设置发件人
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()                       # 实例化Python邮件的smtp类
        s.connect(mail_host)                     # 链接SMTP服务器
        s.login(mail_user, mail_pass)            # 登录服务器
        s.sendmail(me, to_list, msg.as_string()) # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
    
if __name__=='__main__':
    apikey = "e2376cfbe3b27dff923ed61698839a67"
    url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'  # api地址
    req = urllib2.Request(url)             #初始化请求
    req.add_header("apikey", apikey)       #添加http请求的header
    resp = urllib2.urlopen(req)            # 发起请求
    content = resp.read()                  # 获得返回内容， json格式字符串
    if(content):
        json_result = json.loads(content)  # 转换为字典对象
        # 下面从这个字典中获得笑话的标题和正文
        content_list = json_result['showapi_res_body']['contentlist']
        minlen = 10000
        for item in content_list:
            if len(item['text'])< minlen:
                # 只取第一条笑话的标题和正文
                first_title = item['title']
                first_text = item['text']
                minlen = len(item['text'])
        print 'title: ' + first_title
        print 'content:' + first_title
        length = len(first_text)
        part1 = first_text[0:10]
        part2 = first_text[10:22]
        part3 = first_text[22:length]
        print part1, "+", part2, "+", part3
        if send_mail(mailto_list, part1, part2, part3):
            print "send msg succeed"
        else:
            print "send msg failed"   
    else:
        print "get joke error"
         