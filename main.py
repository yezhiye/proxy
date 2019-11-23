import random
import os
import requests
from bs4 import BeautifulSoup as bs

class Daili(object):
    def __init__(self):
        #将考虑建立多个文件夹，考虑多网站多目录情况
        #因代理ip时效性问题，下一步考虑根据配置是否在程序启动时清除之前缓存网页
        pass
        
    def getUA(self):
        #随机从一堆ua中返回一个
        ua = ['Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5', 'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5', 'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10', 'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+', 'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0', 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)', 'UCWEB7.0.2.37/28/999', 'NOKIA5700/ UCWEB7.0.2.37/28/999', 'Openwave/UCWEB7.0.2.37/28/999', 'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999']
        index = random.randint(1,len(ua))
        return ua[index-1]
        
    def caclePages(self,url):
        #判断网页是否已缓存
        #有则直接读取返回
        #无则缓存后返回
        l = url.split('/')
        if l[-1] == '':
            fileName = l[-2]
        else:
            fileName = l[-1]
        #如果url末尾是/，则切割结果为空
        #目前暂不考虑多网站多个目录情况，使用末尾字符串作为文件名
        if os.path.exists(fileName):
            with open(fileName,'r') as f:
                pageContent = f.read()
        else:
            r = requests.get(url)
            pageContent = r.text
            with open(fileName,'w') as f:
                f.write(pageContent)
        return pageContent
        
    def analyze(self,url):
        pageContent = self.caclePages(url)
        soup = bs(pageContent,features="lxml")
        result = soup.tbody.find_all('tr')
        l=[]
        for i in result:
            l.append(i.find_all('td')[0].text)
        return l
           
    def main(self):
        print(self.analyze("http://www.xiladaili.com/https/2/"))
        
daili = Daili()
daili.main()
