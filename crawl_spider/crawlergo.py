import simplejson
import subprocess
import logs.log as Log
import common_config

def crawlergo(target):
    try:
        if("https://" in target):
            proxies = common_config.proxis["https"]
        else:
            proxies = common_config.proxis["http"]
        cmd = [common_config.crawlergoPath, "-c", common_config.ChromePath, "-o", "json",
               "-f", common_config.crawlerFilterMode, "-t", str(common_config.ChromeMaxTab), "--request-proxy", proxies, target]
        # cmd = ["./crawlergo_darwin_arm64", "-c", "/usr/bin/chromedriver", "-o", "json", target]
        # crawlergo地址                                           谷歌浏览器地址
        rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        Log.Info("开始爬取\t" + target)
        output, error = rsp.communicate()
        # "--[Mission Complete]--"  is the end-of-task separator string
        if output:
            result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
            r = result["req_list"]
            urls = []
            for crawlurl in r:
                urls.append(crawlurl['url'])
            return urls
        else:
            Log.Error(target + "\t无法访问")
            return []
    except Exception as e:
        Log.Error(target + "\t爬取错误")
        print(e)
        return False
