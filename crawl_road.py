# -*- coding: utf-8 -*-
# @Time : 2020/2/4 19:04
# @Author : 番茄炒鸡蛋
import requests
import pandas as pd
import json
import time
import datetime
import os
try:
    os.mkdir('指定线路爬虫数据结果')
except:
    pass
pqsj=12
for m in range(pqsj):
    start_time = datetime.datetime.now()
    key='71619826eeac82b250aa007a2de7ec45'
    cityname='成都'
    roadName ='人民南路三段'
    url = 'https://restapi.amap.com/v3/traffic/status/road?key=' + key + '&extensions=all&name=' + roadName + '&city=' + cityname
    x = []
    num = 0
    try:
        data = requests.get(url)
        s = data.json()
        a = s["trafficinfo"]["roads"]  # trafficinfo表示“交通态势信息”，后面并没用到，考虑是否删除，roads表示“道路信息“，其中包括polyline”道路坐标集，坐标集合“
        for k in range(0, len(a)):
            s2 = a[k]["polyline"]  # polyline”表示从列表集a中的roads信息中抽取polyline道路坐标集，坐标集合“
            s3 = s2.split(";")
            for l in range(0, len(s3)):
                s4 = s3[l].split(",")
                x.append([a[k].get('name'), a[k].get('status'), a[k].get('direction'), a[k].get('angle'),
                          a[k].get('speed'), num, float(s4[0]), float(s4[1])])
            num = num + 1  # name表示 道路名称'status'表示路况0：未知1：畅通2：缓行3：拥堵4：严重拥堵 'speed'表示 速度——km/h
    except Exception as e:  # 不用管一样能够运行
        pass
    c = pd.DataFrame(x)
    c.to_csv('./指定线路爬虫数据结果/' + str(m) + '.csv', mode='a', encoding='utf-8-sig',
             header=['路名', '拥堵状态', '方向描述', '行车角度', '车速', '路段ID', '经度', '纬度'])
    print("完成文件" + str(m) + "的爬取")
    end_time = datetime.datetime.now()      #放在程序结尾处
    interval = (end_time-start_time).seconds   #以秒的形式
    print("开始时间:\t",start_time,"\n","结束时间:\t",end_time,"\n","爬取时间:\t", interval,"秒")
    time.sleep(300 - interval)
print("爬取完毕")
