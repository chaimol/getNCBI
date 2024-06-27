#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#脚本的目的是输入NCBI的SRA的编号，输出该编号对应的所有SRR号的下载地址。
#运行方法：python3 getSRA.py PRJNA513297
#https://trace.ncbi.nlm.nih.gov/Traces/sra-db-be/sra-db-be.cgi?rettype=acclist&WebEnv=MCID_62d67537fe2ed559b6fc7848&query_key=1

import sys
import requests,random
#import csv
from bs4 import BeautifulSoup
#https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA513297
#https://www.ncbi.nlm.nih.gov/gene/?term=Zm00001d036521
#payload={'term':'PRJNA513297'}
#genename='Zm00001d036521'
#读取输入的参数
if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("Ussage:python3 getSRA.py PRJNA513297 \n 每次只能输入一个编号，可以是项目编号或SRP号")
    sys.exit(1)
else:
    genename=sys.argv[1]

#反反爬虫部署，添加headers,random访问，增加代理，使用代理访问。
user_agents=['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'] 
def getGid(genename): 
    #files={'file':open('deg.csv','rb')}
    payload={'term':genename}
    headers={'User-Agent':random.choice(user_agents)}
    proxies={'http':'74.59.132.126:49073','https':'74.59.132.126:49073'}
    url="https://www.ncbi.nlm.nih.gov/sra/"
    #req=requests.get(url,headers=headers,params=payload,proxies=proxies)
    req=requests.get(url,headers=headers,params=payload)
    html=req.text
    bf=BeautifulSoup(html,"html5lib")
    a=bf.find_all(id='id-sra-run-selector-popup') 
    #获得链接地址
    href=a[0].get("href")
    #提取MCID和query_key,并拼接
    gid = href.split("/")[3].replace("?","https://trace.ncbi.nlm.nih.gov/Traces/sra-db-be/sra-db-be.cgi?rettype=acclist&")
    print(gid)
    #return gid

getGid(genename)

# genecount=csv.reader(open('deg.csv','r'))

# gene_table=['gid']
# locus=['genename']

# for geneid in genecount:
    # print(geneid[0])
    # gid=getGid(geneid[0])
    # gene_table.append(gid)
    # locus.append(geneid)
    # time.sleep(random.random()) #暂停[0,1)秒

# with open('out.csv','w',newline='') as f:
    # writer=csv.writer(f)
    # for row in gene_table:
        # writer.writerow(row)


