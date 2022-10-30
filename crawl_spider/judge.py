import requests
from bs4 import BeautifulSoup
import common_config
from crawl_spider import crawlergo
import logs.log as Log

spider_start_info = '''
+---------------------------------------------------+
|                     启动爬虫模块                    |
+---------------------------------------------------+
'''

def judge(Url):  # 初次判断是否为登录页面
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    try:
        web_data = requests.get(Url, headers=Headers, proxies=common_config.proxis, timeout=10, verify=False)
        soup = BeautifulSoup(web_data.text, features="lxml")
        soup = soup.text.lower()

        if (("登录" in soup)\
            or ("login" in soup)\
            or ("password" in soup)\
            or ("密码" in soup)\
            or ("用户名" in soup)\
            or ("管理系统" in soup)\
            or ("username" in soup)):
            return True
        else:
            return False
    except Exception as e:
        Log.Error(e)
        return False


def spiderRun(url):
    print(spider_start_info)
    loginurl = []
    SpiderResult = crawlergo.crawlergo(url)
    if not SpiderResult:
        return loginurl

    Log.Info(url+"\t爬取完成，开始初步登录页面分析...")
    for SpiderResulturl in SpiderResult:
        if (judge(SpiderResulturl)):
            loginurl.append(SpiderResulturl)
    if (loginurl != []):
        Log.Info(url + "\t初步判断存在登录页面")
    else:
        Log.Info(url + "\t未发现登录页面")
    return loginurl
