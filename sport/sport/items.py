# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class SportItem(scrapy.Item):
    #NBA
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    playerteam = scrapy.Field ()  #球队
    playerimg = scrapy.Field ()   #球员照片
    playername = scrapy.Field ()  #球员姓名
    playernumber = scrapy.Field ()   #球员号码
    playerjob = scrapy.Field ()      #球员位置
    playertall = scrapy.Field ()     #球员身高
    playerweight = scrapy.Field ()   #球员体重
    playerbirthday = scrapy.Field () #球员生日
    playercont = scrapy.Field ()   #球员合同
    playersal = scrapy.Field ()    #球员年薪  
    
class footballItem(scrapy.Item):
    #足球
    league = scrapy.Field ()        #联赛名称
    team_name = scrapy.Field ()     #球队名称
    player_number = scrapy.Field ()     #球员号码
    player_cha_name = scrapy.Field ()  #球员中文名
    player_eng_name = scrapy.Field ()  #球员英文名
    player_age = scrapy.Field ()       #球员年龄
    player_courtry = scrapy.Field ()  #球员所属国籍
    player_job  = scrapy.Field ()     #球员位置 
    
    team_logo  = scrapy.Field ()    #球队logo
    team_coach = scrapy.Field ()    #球队教练
    team_build = scrapy.Field ()    #成立时间
    team_city  = scrapy.Field ()    #所在城市
    team_place = scrapy.Field ()    #主球场
    team_addr  = scrapy.Field ()    #联系地址 
    team_href  = scrapy.Field ()    #官网 
    
class footballRank(scrapy.Item):
    #足球联赛积分榜
    league = scrapy.Field()         #联赛名称
    rank  = scrapy.Field()          #排名
    team_name = scrapy.Field()      #球队名称
    play = scrapy.Field()       #场次
    win = scrapy.Field()        #胜
    same = scrapy.Field()       #平
    loss = scrapy.Field()       #负
    all_win_ball = scrapy.Field()    #进球
    loss_ball= scrapy.Field ()       #失球
    goal_ball = scrapy.Field ()      #净胜球
    score = scrapy.Field ()          #积分  
    
class footballScores(scrapy.Item):
    #足球联赛射手榜
    league = scrapy.Field()         #联赛名称
    rank = scrapy.Field()           #排名
    team_name = scrapy.Field()      #球队名称
    player_cha = scrapy.Field()     #中文名
    player_eng = scrapy.Field()     #英文名
    player_job = scrapy.Field()     #位置
    coming_ball = scrapy.Field()    #进球数
    penalty_ball = scrapy.Field()   #点球数    
