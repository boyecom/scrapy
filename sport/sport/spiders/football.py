# -*- coding: utf-8 -*-
import scrapy
from  sport.items import footballItem

class FootballSpider(scrapy.Spider):
    name = 'football'
    allowed_domains = ['soccer.hupu.com']
    start_urls = ['http://soccer.hupu.com/']

    def parse(self, response):
        #获取联赛
        league_title = response.xpath('//li[@class="hp-dropDownMenu"][position()<=4]/a/@title').extract()
        league_url = response.xpath('//li[@class="hp-dropDownMenu"][position()<=4]/a/@href').extract()
        for title,url in zip(league_title,league_url):
            yield scrapy.Request(url=url, meta={'league': title}, 
                                    callback=self.team_detail,dont_filter=True) 
    def team_detail(self,response):
        #获取球队
        league = response.meta.get('league')
        for team in response.xpath('//ul[@class="england-list-item"]/li'):
            team_url = team.xpath("a/@href").extract()
            team_name = team.xpath("a/@title").extract()
            team_url = team_url[0] if team_url else ''
            team_name = team_name[0] if team_name else ''
            #print(team_name,team_url)
            if not team_url:
                continue
            yield scrapy.Request(url=team_url, meta={'league': league,'team_name':team_name}, 
                                    callback=self.player_detail,dont_filter=True)  
            
    def player_detail(self,response):
        #获取球员
        league = response.meta.get('league')
        team_name = response.meta.get('team_name')
        #team_name = response.xpath("//div[@class='team_info left']/h3/span/text()").extract_first("")
        team_logo = response.xpath("//li[@class=' left pic_logo']/img/@src").extract_first("")
        team_coach =response.xpath("//div[@class='team_info left']//dl[@class='clearfix']/dd[1]/text()").extract_first("")
        team_build = response.xpath("//div[@class='team_info left']//dl[@class='clearfix']/dd[2]/text()").extract_first("")
        team_city = response.xpath("//div[@class='team_info left']//dl[@class='clearfix']/dd[3]/text()").extract_first("")
        team_place = response.xpath("//div[@class='team_info left']/ul[2]/li[1]/text()").extract_first("")
        team_addr = response.xpath("//div[@class='team_info left']/ul[2]/li[2]/text()").extract_first("")
        team_href = response.xpath("//div[@class='team_info left']/ul[2]/li/a/@href").extract_first("")
        for playinfo in response.xpath('//table[@class="team_player"]'):
            #print(playinfo.xpath('//tr[not(@calss)]'))
            
            
            for player in playinfo.xpath('tr'):
                #print(player)
                player_number = player.xpath("td[1]/text()").extract()
                player_cha_name = player.xpath("td[2]/a/text()").extract()
                player_eng_name = player.xpath("td[3]/a/text()").extract()
                player_age = player.xpath("td[4]/text()").extract()
                player_courtry = player.xpath("td[5]/text()").extract()
                player_job = player.xpath("td[6]/text()").extract()
                #player_job = player.xpath("td[6]/text()").extract_first("")
                
                player_number = player_number[0] if player_number else ''
                player_cha_name = player_cha_name[0] if player_cha_name else ''
                player_eng_name = player_eng_name[0] if player_eng_name else ''
                player_age = player_age[0] if player_age else ''
                player_courtry = player_courtry[0] if player_courtry else ''
                player_job = player_job[0] if player_job else ''
                #print(player_number,player_cha_name,player_eng_name,player_age,player_courtry,player_job)
                if not player_number.isdigit():
                    continue
                item = footballItem()
                item['league'] = league #联赛名称
                item['team_name'] = team_name     #球队名称
                item['player_number'] = player_number   #球员号码
                item['player_cha_name'] = player_cha_name  #球员中文名
                item['player_eng_name'] = player_eng_name #球员英文名
                item['player_age'] = player_age       #球员年龄
                item['player_courtry'] = player_courtry  #球员所属国籍
                item['player_job'] = player_job #球员位置
                item['team_logo'] = team_logo   #球队logo
                item['team_coach'] = team_coach #球队教练
                item['team_build'] = team_build #成立时间
                item['team_city'] = team_city   #所在城市
                item['team_place'] = team_place #主球场
                item['team_addr'] = team_addr   #联系地址 
                item['team_href'] = team_href   #官网              
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

