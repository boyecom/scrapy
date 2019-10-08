#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import hashlib
from  sport.DB import MysqlDB
from  sport.items import SportItem,footballItem,footballRank,footballScores

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SportPipeline(object):
    def __init__(self):
        self.db=None    
        self.filename = open('sport.json','w',encoding='utf-8')
        
    def get_md5(self,SecretKey):
        #md5加盐
        SecretKey = SecretKey.encode('utf-8')
        m = hashlib.md5(SecretKey)
        return m.hexdigest()
    
    def write_data(self, item):
        text = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.filename.write(text)        
           
    
    def process_item(self, item, spider):
        #处理数据
        print('=======正在处理==========')
        d =dict(item)
        keys=str(tuple(d.keys()))
        keys = keys.replace("'","")
        sql=None
        if isinstance(item, SportItem):
            sql ="REPLACE INTO PLAYER_INFO{} VALUES{}".format(keys,str(tuple(d.values())))
        elif isinstance(item, footballItem):
            sql ="REPLACE INTO FOOTBALL_INFO{} VALUES{}".format(keys,str(tuple(d.values())))
        elif isinstance(item, footballRank):
            sql ="REPLACE INTO FOOTBALL_RANK{} VALUES{}".format(keys,str(tuple(d.values())))
        elif isinstance(item, footballScores):
            sql ="REPLACE INTO FOOTBALL_SCORES{} VALUES{}".format(keys,str(tuple(d.values())))        

        self.db.execute(sql) 
        print("执行[{}]成功".format(sql))
        #self.write_data(item)
        return item
    
    def open_spider(self, spider):
        #该方法在spider被开启时被调用。
        host = spider.settings.get('HOST')
        username = spider.settings.get('USERNAME')
        password = spider.settings.get('PASSWORD')
        database = spider.settings.get('DATABASE')
        self.db = MysqlDB(host,username,password,database)
        print('=========爬虫启动=======')
        return 0  
    
    def close_spider(self, spider):
        #该方法在spider被关闭时被调用。
        self.filename.close()
        print('==========爬取完毕！========')
        
        
class footballPipeline(SportPipeline):
    #足球
    def __init__(self):
        self.db=None    
        self.filename = open('football.json','w',encoding='utf-8') 
        
    def process_item(self, item, spider):
        #处理数据
        print('=======正在处理==========')
        d =dict(item)
        keys=str(tuple(d.keys()))
        keys = keys.replace("'","")
        sql ="REPLACE INTO FOOTBALL_INFO{} VALUES{}".format(keys,str(tuple(d.values())))
        #print(sql)
        self.db.execute(sql) 
        print("执行[{}]成功".format(sql))
        self.write_data(item)
        return item