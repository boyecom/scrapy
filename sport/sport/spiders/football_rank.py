# -*- coding: utf-8 -*-
import scrapy
from  sport.items import footballRank

class FootballRankSpider(scrapy.Spider):
    """联赛积分榜"""
    name = 'football_rank'
    allowed_domains = ['soccer.hupu.com']
    start_urls = ['https://soccer.hupu.com/table/']

    def parse(self, response):
        #获取联赛积分榜
        url_list = response.xpath('//ul[@class="score-tab"]/li/a/@href').extract()
        league_list =  response.xpath('//ul[@class="score-tab"]/li/a/text()').extract()
        league_list = [ ''.join(league.split()) for league in league_list]
        for url,leage in zip(url_list,league_list):
            yield scrapy.Request(url=url, meta={'league':leage}, 
                                    callback=self.team_detail,dont_filter=True) 
    def team_detail(self,response):
        league = response.meta.get('league')
        for team in  response.xpath("//table[@id='main_table']/tbody/tr[@class]"):
            rank = team.xpath("td[1]/text()").extract_first("") #排名
            rank = int(rank) if rank.strip().isdigit() else ''
            team_name = team.xpath("td[3]/a/text()").extract_first("") #球队名
            #team_url = team.xpath("td[3]/a/@href").extract_first("") #球队链接
            play = team.xpath("td[4]/text()").extract_first("") #场次
            win = team.xpath("td[5]/text()").extract_first("")  #胜
            same = team.xpath("td[6]/text()").extract_first("") #平
            loss = team.xpath("td[7]/text()").extract_first("") #负
            all_win_ball = team.xpath("td[8]/text()").extract_first("") #进球
            loss_ball = team.xpath("td[9]/text()").extract_first("") #失球
            goal_ball = team.xpath("td[10]/text()").extract_first("") #净胜球
            score = team.xpath("td[15]/text()").extract_first("") #积分
            
            item = footballRank()
            item['league'] = league
            item['rank'] = rank
            item['team_name'] = team_name
            item['play'] = play
            item['win'] = win
            item['same'] = same
            item['loss'] = loss
            item['all_win_ball'] = all_win_ball
            item['loss_ball'] = loss_ball
            item['goal_ball'] = goal_ball
            item['score'] = score
            
            
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

