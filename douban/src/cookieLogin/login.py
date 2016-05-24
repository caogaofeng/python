# -*- coding: utf-8 -*-
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
  
#鐧诲綍鐨勪富椤甸潰  
hosturl = 'https://www.douban.com/accounts/login?redir=http%3A//www.douban.com/people/czhyj912/rev_contacts' 
#鑷繁濉啓  
#post鏁版嵁鎺ユ敹鍜屽鐞嗙殑椤甸潰锛堟垜浠鍚戣繖涓〉闈㈠彂閫佹垜浠瀯閫犵殑Post鏁版嵁锛�  
posturl = '******' 
#浠庢暟鎹寘涓垎鏋愬嚭锛屽鐞唒ost璇锋眰鐨剈rl  
  
#璁剧疆涓�涓猚ookie澶勭悊鍣紝瀹冭礋璐ｄ粠鏈嶅姟鍣ㄤ笅杞絚ookie鍒版湰鍦帮紝骞朵笖鍦ㄥ彂閫佽姹傛椂甯︿笂鏈湴鐨刢ookie  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
#鎵撳紑鐧诲綍涓婚〉闈紙浠栫殑鐩殑鏄粠椤甸潰涓嬭浇cookie锛岃繖鏍锋垜浠湪鍐嶉�乸ost鏁版嵁鏃跺氨鏈塩ookie浜嗭紝鍚﹀垯鍙戦�佷笉鎴愬姛锛�  
h = urllib2.urlopen(hosturl)  
  
#鏋勯�爃eader锛屼竴鑸琱eader鑷冲皯瑕佸寘鍚竴涓嬩袱椤广�傝繖涓ら」鏄粠鎶撳埌鐨勫寘閲屽垎鏋愬緱鍑虹殑銆�  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : '******'}  
#鏋勯�燩ost鏁版嵁锛屼粬涔熸槸浠庢姄澶х殑鍖呴噷鍒嗘瀽寰楀嚭鐨勩��  
postData = {'op' : 'dmlogin',  
            'f' : 'st',  
           'user' : '******', #浣犵殑鐢ㄦ埛鍚�  
            'pass' : '******', #浣犵殑瀵嗙爜锛屽瘑鐮佸彲鑳芥槸鏄庢枃浼犺緭涔熷彲鑳芥槸瀵嗘枃锛屽鏋滄槸瀵嗘枃闇�瑕佽皟鐢ㄧ浉搴旂殑鍔犲瘑绠楁硶鍔犲瘑  
            'rmbr' : 'true',   #鐗规湁鏁版嵁锛屼笉鍚岀綉绔欏彲鑳戒笉鍚�  
            'tmp' : '0.7306424454308195'  #鐗规湁鏁版嵁锛屼笉鍚岀綉绔欏彲鑳戒笉鍚�  
  
            }  
  
#闇�瑕佺粰Post鏁版嵁缂栫爜  
postData = urllib.urlencode(postData)  
  
#閫氳繃urllib2鎻愪緵鐨剅equest鏂规硶鏉ュ悜鎸囧畾Url鍙戦�佹垜浠瀯閫犵殑鏁版嵁锛屽苟瀹屾垚鐧诲綍杩囩▼  
request = urllib2.Request(posturl, postData, headers)  
print request  
response = urllib2.urlopen(request)  
text = response.read()  
print text
