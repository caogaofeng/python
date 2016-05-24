#encoding=utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import sys
import sql
import time
import random
import cookielib

class login_page:
    def login(self):
        #loginUrl = 'https://www.douban.com/accounts/login?redir=http%3A//www.douban.com/people/vicce/statuses'
        #loginUrl = 'https://www.douban.com/accounts/login?redir=http%3A//www.douban.com/people/lcaesar/statuses'
        type = sys.getfilesystemencoding()
        formData={
            #"redir":"http://movie.douban.com/mine?status=collect",
            "redir":"http://www.douban.com/login",
            "form_email":"401681050@qq.com",
            "form_password":"gaofeng0215",
            "login":u'登录'
        }
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36' 
                    ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                    ,'Accept-Encoding':'gzip,deflate,sdch'
                    ,'Accept-Language':'zh-CN,zh;q=0.8'
                    ,'Cache-Control':'max-age=0'
                    ,'Connection':'keep-alive'
                    #,'Content-Type':'text/html,charset=utf-8'
                    #,'Content-Encoding':'gzip'
        }
        time.sleep(int(random.uniform(5, 10)))
        s = requests.session() 
        #s.post("http://www.douban.com/login",data=formData,headers=headers)
        r = s.post("http://www.douban.com/login",data=formData,headers=headers)
        page = r.text
        '''获取验证码图片'''
        #利用bs4获取captcha地址
        soup = BeautifulSoup(page,"html.parser")
        captchaAddr = soup.find('img',id='captcha_image')['src']
        #利用正则表达式获取captcha的ID
        reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
        captchaID = re.findall(reCaptchaID,page)
        #print captchaID
        #保存到本地
        urllib.urlretrieve(captchaAddr,"captcha.jpg")
        captcha = raw_input('please input the captcha:')
        
        formData['captcha-solution'] = captcha
        formData['captcha-id'] = captchaID
        s.post("http://www.douban.com/login",data=formData,headers=headers)
        #r = requests.post(reUrl,data=formData,headers=headers)
        #time.sleep(int(random.uniform(3, 5)))
        #r = s.get(url)
        #print r.text
        return s
        #print r.url