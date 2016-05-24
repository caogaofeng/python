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
    def login(self,url):
        #loginUrl = 'https://www.douban.com/accounts/login?redir=http%3A//www.douban.com/people/vicce/statuses'
        #loginUrl = 'https://www.douban.com/accounts/login?redir=http%3A//www.douban.com/people/lcaesar/statuses'
        if 'redir=' in url:
            reUrl = url.split('redir=')[1].replace('%3A',':')
        else:
            reUrl = url
        type = sys.getfilesystemencoding()
        formData={
            #"redir":"http://movie.douban.com/mine?status=collect",
            "redir":reUrl,
            "form_email":"401681050@qq.com",
            "form_password":"gaofeng0215",
            "login":u'登录'
        }
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        time.sleep(int(random.uniform(1, 1)))
        r = requests.post(reUrl,data=formData,headers=headers)
        page = r.text
        print "li mian:"+r.url
        #print page
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
        time.sleep(int(random.uniform(1, 1)))
        r = requests.post(r.url,data=formData,headers=headers)
        return r
        #print r.url