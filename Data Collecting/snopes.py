import numpy as np
import pandas as pd
import requests
from collections import Counter
import urllib
import re
import traceback
from bs4 import BeautifulSoup
import datetime
import json
header = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }

def getHTMLText(url, code="utf-8"):
    try:
        html = requests.get(url, headers=header)
        html.raise_for_status()
        html.encoding = code
        return html.text
    except:
        return ""
class SpiderRumor(object):
    def __init__(self):
        self.snops = "https://www.snopes.com/tag/covid-19/page/%d/"
        self.piyao = "http://qc.wa.news.cn/nodeart/list?nid=11215616&pgnum=%d&cnt=10&attr=63"        

    def spider_piyao(self):
        df_all = list()
        for url in [self.piyao % i for i in range(1,60)]:
            try:
                data_list = requests.get(url, headers=header).text#.json()content.json()['list']
                data_list=data_list.replace("(",'').replace(")",'')
                data_list=json.loads(data_list)['data']['list']
                print(url)
                temp_data = [[df["Title"], df["PubTime"], df["SourceName"], df["keyword"], df["LinkUrl"]]
                        for df in data_list]
                df_all.extend(temp_data)
            except:
                continue

        # generate csv
        df = pd.DataFrame(df_all, columns=["title", "date", "author", "result", "id"])
        time = df['date']
        for i in range(len(time)):
            time[i] = datetime.datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S")
            time[i] = time[i].strftime('%m/%d/%Y')
        df.drop_duplicates(subset='id', inplace=True)
        df.to_csv("rumor_piyao_chinese_original.csv", encoding="utf_8_sig")
    def spider_run(self):
        link = list()
        df_all=list()
        for url in [self.snops % i for i in range(1,8)]:
            try:
                html=getHTMLText(url)
                soup=BeautifulSoup(html,"html.parser")
                article=soup.find_all('article',attrs={'class':'media-wrapper'})
                for i in range(len(article)):
                    try:
                        j=article[i].a
                        herf=j.attrs['href']
                        link.append(herf)
                    except:
                        continue
            except:
                continue
        for url in link:
            html=getHTMLText(url)
            try:
                if html=='':
                    continue
                soup = BeautifulSoup(html, "html.parser")
                title=soup.find_all('div',attrs={'class':'claim'})[0].p.text
                date=soup.find_all('span',attrs={'class':'date date-published'})[0].text
                author=soup.find('a',attrs={'class':'author'}).text
                result=soup.find('div',attrs={'class':'media rating'}).div.h5.text
                temp_data=[title,date,author,result,url]
                df_all.append(temp_data)
                print(url+'finish')
            except:
                print('false')
                continue
        df = pd.DataFrame(df_all, columns=["title", "date", "author", "result", "id" ])
        df.drop_duplicates(subset='id', inplace=True)
        df.to_csv("rumor_snopes_original.csv", encoding="utf_8_sig")

def convert():
    df = pd.DataFrame(pd.read_csv('rumor_snopes_original.csv'))
    result=df['result']
    print(Counter(result))
    for i in range(len(result)):
        result[i]=result[i].replace('Mixture','fake').replace('Mostly False','fake').replace('False','fake').replace('True','true')\
            .replace('Unproven','unverified').replace('Correct Attribution','true').replace('Miscaptioned','fake')\
            .replace('Labeled Satire','fake').replace('Outdated','fake')
    print(Counter(result))
    time=df['date']
    for i in range(len(time)):
        time[i]=datetime.datetime.strptime(time[i],"%d %B %Y")
        time[i]=time[i].strftime('%m/%d/%Y')
    df.drop_duplicates(subset='id', inplace=True)
    df.to_csv("rumor_snopes_modified.csv", encoding="utf_8_sig")

def remove_old():
    df = pd.DataFrame(pd.read_csv('rumor_wechat_chinese_original.csv'))
    date=df['date']
    d1=datetime.datetime.strptime('2019-12-01','%Y-%m-%d')
    for i in range(len(date)):
        d2=datetime.datetime.strptime(date[i],'%Y-%m-%d')
        if d2<d1:
            df.drop([i],inplace=True)
    df.to_csv('rumor_wechat_chinese_RemoveOldData.csv',encoding="utf_8_sig")

def count_tag(filename,modify=0):
    df = pd.DataFrame(pd.read_csv(filename))
    if modify:
        result = df['result']
        for i in range(len(result)):
            result[i] = result[i].replace('FALSE','fake').replace('TRUE','true').replace('suspect','unverified')
    print(Counter(df['result']))
    df.to_csv(filename,encoding="utf_8_sig")
if __name__ == '__main__':
    spider = SpiderRumor()
    spider.spider_run()
    convert()
    remove_old()
    #count_tag('rumor_wechat_english_translated.csv',modify=1)
    #spider.spider_piyao()
    #count_tag('rumor_piyao_english_original.csv')
    #df = pd.DataFrame(pd.read_csv('all.csv'))
    #print(Counter(df['result']))
