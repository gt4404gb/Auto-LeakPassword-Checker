import pandas as pd
import re

class putlist:
    reg = r'http(\w)?'
    # 匹配http
    def putexcel(self,filename):
        # 使用该方法读取excel网址，需输入文件名例如：baidu.txt
        df = pd.read_excel(filename)
        # 读取excel文件
        list_url = []
        # list_url存放最后的网址
        url_list = list(df.values)
        # url_list存放excel中的数据
        for temp in url_list:
            # 取excel中出每行数据
            for temp2 in temp:
                m = re.match(self.reg, str(temp2))
                # 匹配http
                if m == None:
                    continue
                url = self.replace_uri(temp2)
                url = url.replace('\r','').replace('\n','')
                list_url.append(url)
        #         将存在http的信息放入列表中
        return  list_url
#       该方法返回一个存放网址的列表

    def puttxt(self,filename):
        # 使用该方法读取txt网址，需输入文件名例如：baidu.txt
        list_url=[]
        with open(filename,'r',encoding='utf-8') as file:
            # 打开txt文件
            url_list = file.readlines()
            # 按行读取放入url_list列表中
            for temp in url_list:
                # 循环读取txt每行数据
                templist = temp.split('\t')
                # 按空格分割
                for temp in templist:
                    m = re.match(self.reg, str(temp))
                    # 匹配http网址
                    if m == None:
                        continue
                    url = self.replace_uri(temp)
                    url = url.replace('\r','').replace('\n','')
                    list_url.append(url)
                    #         将存在http的信息放入列表中
            return list_url
        #       该方法返回一个存放网址的列表

    def putcsv(self,filename):
        # 使用该方法读取excel网址，需输入文件名例如：baidu.txt
        df = pd.read_csv(filename, encoding = 'gb2312')
        # 读取csv文件
        list_url = []
        # list_url存放最后的网址
        url_list = list(df.values)
        # url_list存放csv中的数据
        for temp in url_list:
            # 取csv中出每行数据
            for temp2 in temp:
                m = re.match(self.reg, str(temp2))
                # 匹配http
                if m == None:
                    continue
                url = temp2
                url = url.replace('\r', '').replace('\n', '')
                list_url.append(url)
        #         将存在http的信息放入列表中
        return list_url

    def replace_uri(self,url):
        if('?' in url):
            replaceurl = url.split('?')[0]
            return replaceurl
        else:
            return url

def formattext(file):
    print("导入域名文件...")
    text = putlist()
    try:
        if ".xls" in file:
            FormatWebSite = text.putexcel(file)
            print("导入文件成功！")
            return FormatWebSite
        elif ".csv" in file:
            FormatWebSite = text.putcsv(file)
            print("导入文件成功！")
            return FormatWebSite
        elif ".txt" in file:
            FormatWebSite = text.puttxt(file)
            print("导入文件成功！")
            return FormatWebSite
    except:
        print("导入文件错误")
        exit(0)

    else:
        print("输入文件错误")
        exit(0)
