from crawl_spider import judge,crawlergo
from auto_login import webcrack
from input_format import txt_excel
import logs.log as Log
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "url.txt"
    #格式化文本
    FormatWebSite = txt_excel.formattext(file)
    #格式化之后对网站进行顺序爬取
    count = 1
    for website in FormatWebSite:
        Log.init_log_id(count)
        count = count + 1
        try:
            resulturl = judge.spiderRun(website)
            #启动爆破模块
            if resulturl != [] :
                resulturl = list(set(resulturl)) #列表去重
                webcrack.run_crack(resulturl)
        except Exception as e:
            print(e)
            continue

    exit(0)
