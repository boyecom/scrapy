# -*- coding: utf-8 -*-
import scrapy
from  sport.items import footballScores

class FootballScoreSpider(scrapy.Spider):
    """联赛射手榜"""
    name = 'football_score'
    allowed_domains = ['soccer.hupu.com']
    start_urls = ['https://soccer.hupu.com/scorers/']

    def parse(self, response):
        #获取联赛射手榜
        url_list =  response.xpath("//div[@class='jftag']/ul/li/a/@href").extract()
        league_list =  response.xpath("//div[@class='jftag']/ul/li/a/span/text()").extract()
        league_list = [ ''.join(league.split()) for league in league_list]
        for url,leage in zip(url_list,league_list):
            yield scrapy.Request(url=url, meta={'league':leage}, 
                                    callback=self.team_detail,dont_filter=True) 
            
    def team_detail(self,response):
        league = response.meta.get('league')
        for info in response.xpath("//div[@class='jf']/table//tr[@class='trbgwhite']"):
            rank = info.xpath("td[1]/text()").extract_first("") #排名
            rank = int(rank) if rank.strip().isdigit() else ''
            player_cha = info.xpath("td[2]/text()").extract_first("").strip() #中文名
            player_eng = info.xpath("td[3]/text()").extract_first("").strip() #英文名
            team_name = info.xpath("td[4]/text()").extract_first("").strip() #俱乐部
            player_job = info.xpath("td[5]/text()").extract_first("").strip() #位置
            coming_ball = info.xpath("td[6]/text()").extract_first("").strip() #进球数 
            penalty_ball = info.xpath("td[7]/text()").extract_first("").strip() #点球数
            item = footballScores()
            
            item['league'] = league
            item['rank'] = rank
            item['player_cha'] = player_cha
            item['player_eng'] = player_eng
            item['team_name'] = team_name
            item['player_job'] = player_job
            item['coming_ball'] = coming_ball
            item['penalty_ball'] = penalty_ball
            yield item
           
    
           
            
    
                
                
if __name__ == '__main__':
    from lxml import etree
    
    path="E:/youbest/project/spider/sport/football.html"
    fd = open(path,'rb')
    html = fd.read()
    response = etree.HTML(html)
    #print(response.text)
    d=response.xpath('//table[@class="team_player"]')
    #print(d)

