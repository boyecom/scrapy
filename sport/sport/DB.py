#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymysql as sql
#import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import traceback

# ============================================
# Function:数据库操作
# Author:lby
# Create:2019-01-24
#
# History:
#  <author>   <time>      <desc>
#
# ============================================

class DB:
    """
    数据库操作
    create_engine("dialect+driver://username:password@host:port/database") #初始化连接
    dialect:数据库类型，包括sqlite,mysql,postgresql,oracle,mssql等
    driver:指定连接数据库的API,如 psycopg2,pyodbc,cx_oracle,为可选关键字
    """
    engine = None
        
    def session(self):
        try:
            dbSession = sessionmaker(bind=self.engine)
            cursor = dbSession()
        except Exception as e :
            print('DataBase found errors: {0}'.format(e))
        return cursor    
    
    def query(self,sql):
        #执行查询语句
        try:
            query = self.session()
            ret = query.execute(sql)
            data = ret.fetchall() 
            return data
        except:
            print(traceback.format_exc())
            print('查询数据异常')
            return []
        
    def execute(self,sql):
        #执行单条语句
        try:
            execute = self.session()
            ret = execute.execute(sql)
            execute.commit()
            execute.close()            
            return 0
        except:
            print('执行[%s]失败'%sql)
            execute.rollback()
            execute.close()
            return -1 
        
    def execute_many(self,SqlList):
        #执行多条sql
        try:
            execute = self.session()
            for sql in SqlList:
                    ret = execute.execute(sql)
            execute.commit()
            execute.close()
            return 0
        except:
            print('执行[%s]失败'%sql)
            execute.rollback()
            execute.close()            
            return -1 
        
class MysqlDB(DB):
    """mysql数据库"""
    def __init__(self,host,user,passwd,database,port=3306):
        url = 'mysql+pymysql://{username}:{passwd}@{host}:{port}/{database}?charset=utf8'.format(username=user,passwd=passwd,host=host,port=port,database=database)
        self.engine = create_engine(url,encoding='utf8',pool_size=100, pool_recycle=3600, echo=False)
        
class OracleDB(DB):
    """Oracle数据库"""
    def __init__(self,host,username,passwd,dsn,port=1521):
        url = 'oracle+cx_oracle://{username}:{passwd}@{host}:{port}/{dsn}?charset=utf8'.format(username=username,passwd=passwd,host=host,port=port,dsn=dsn)
        self.engine = create_engine(url,encoding='utf8',pool_size=100, pool_recycle=3600, echo=False)
        
        
if __name__ == '__main__':
    mysql = MysqlDB('127.0.0.1','root','123456','boye')
    ret = mysql.query('show tables')
    print(ret)
    #mysql.execute('drop table test')
    sql="""CREATE TABLE SCRAPY.LINUXIDC(
           ID VARCHAR(32) PRIMARY KEY  COMMENT 'ID',
           NAME VARCHAR(100) COMMENT '名称',
           URL VARCHAR(200) COMMENT '网址链接',
           TEXT1 VARCHAR(100) COMMENT '描述1',
           TEXT2 VARCHAR(100) COMMENT '描述2',
           TEXT3 VARCHAR(100) COMMENT '描述3',
           TEXT4 VARCHAR(100) COMMENT '描述4'
           )ENGINE=INNODB DEFAULT CHARSET=UTF8 COMMENT='LINUX公社'"""   
    mysql.execute(sql)
    #mysql.execute('create table test(d int,name varchar(20))')
    #mysql.execute_many(["insert into test values(1,'tom')","insert into test values(2,'ok')"])
    #ret = mysql.query('select * from test')
    #print(ret)
    
    #orcl = OracleDB('127.0.0.1','scott','123456','orcl')
    
    #orcl.execute_many(["insert into test values(1,'tom','')","insert into test values(2,'ok','')"])
    #ret = orcl.query('select * from test')
    #print(ret)    
    
    
    