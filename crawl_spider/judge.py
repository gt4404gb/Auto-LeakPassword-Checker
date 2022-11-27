import requests
from bs4 import BeautifulSoup
import common_config
from crawl_spider import crawlergo
import logs.log as Log
import crawl_spider.HTMLSimilarity.htmlsimilarity as htmlsimilarity

spider_start_info = '''
+---------------------------------------------------+
|                     启动爬虫模块                    |
+---------------------------------------------------+
'''

def judge(Url):  # 初次判断是否为登录页面
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        if("https://" in Url):
            web_data = requests.get(Url, headers=Headers, proxies=common_config.proxis, timeout=10, verify=False)
        else:
            web_data = requests.get(Url, headers=Headers, proxies=common_config.proxis, timeout=10)
        code = web_data.apparent_encoding  # 获取url对应的编码格式
        web_data.encoding = code
        html = web_data.text
        soup = BeautifulSoup(html, features="lxml")
        soup = soup.text.lower()
        web_data.close()
        if (("登录" in soup)\
            or ("login" in soup) \
            or ("log in" in soup) \
            or ("password" in soup)\
            or ("密码" in soup) \
            or ("密碼" in soup) \
            or ("用户名" in soup)\
            or ("username" in soup)\
            or ("账户" in soup)\
            or ("管理系统" in soup)):
            return True
        else:
            return False
    except Exception as e:
        #屏蔽错误信息
        #Log.Error(e)
        return False

def decodeHtml(Url):
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        if("https://" in Url):
            web_data = requests.get(Url, headers=Headers, proxies=common_config.proxis, timeout=10, verify=False)
        else:
            web_data = requests.get(Url, headers=Headers, proxies=common_config.proxis, timeout=10)
        code = web_data.apparent_encoding  # 获取url对应的编码格式
        web_data.encoding = code
        html = web_data.text
        return html
    except Exception as e:
        print("???")
        return False

def spiderRun(url):
    print(spider_start_info)
    loginurl = []
    SpiderResult = crawlergo.crawlergo(url)
    Log.Info("爬取页面个数："+str(len(SpiderResult)))
    if not SpiderResult:
        return loginurl

    Log.Info(url+"\t爬取完成，开始初步登录页面分析...")
    for SpiderResulturl in SpiderResult:
        if (judge(SpiderResulturl)):
            #判断网页与已存在的登录页面列表是否相似，相似则不加入
            if loginurl != []:
                sign = 0
                for existurl in loginurl:
                    if htmlsimilarity.get_html_similarity(decodeHtml(SpiderResulturl),decodeHtml(existurl)):
                        #print(loginurl,SpiderResulturl)
                        sign = 1
                        break
                if sign == 0:
                    loginurl.append(SpiderResulturl)
            else:
                loginurl.append(SpiderResulturl)
    if (loginurl != []):
        Log.Info(url + "\t初步判断存在登录页面")

    else:
        Log.Info(url + "\t未发现登录页面")
    return loginurl
