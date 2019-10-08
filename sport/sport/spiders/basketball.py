# -*- coding: utf-8 -*-
import scrapy
from  sport.items import SportItem

class BasketballSpider(scrapy.Spider):
    name = 'basketball'
    allowed_domains = ['hupu.com']
    start_urls = ['https://nba.hupu.com/players/rockets']

    def parse(self, response):
        url_list = response.xpath('//span[@class="team_name"]/a/@href').extract()
        playerteam_list = response.xpath('//span[@class="team_name"]/a/text()').extract()
        #print(url_list)
        #print(playerteam_list)
        for url, playerteam in zip(url_list, playerteam_list):
            team_url = url
            #print(playerteam,url)
            yield scrapy.Request(url=team_url, meta={'playerteam': playerteam}, 
                                    callback=self.parse_detail,dont_filter=True)
              
            
    def parse_detail(self, response):
        #print("开始下载...")
        item = SportItem ()
        
        # 球队
        item['playerteam'] = response.meta['playerteam']
        for d in response.xpath("//tr[not(@class)]"):
            #print(d)
            player_url= d.xpath('td[@class="td_padding"]//a/@href').extract()
            player_img= d.xpath('td[@class="td_padding"]//img/@src').extract()
            player_name = d.xpath('td[@class="left"][1]//a/text()').extract()
            player_number = d.xpath('td[3]/text()').extract()
            player_job = d.xpath('td[4]/text()').extract()
            player_tall = d.xpath('td[5]/text()').extract()
            player_weight = d.xpath('td[6]/text()').extract()
            player_birthday = d.xpath('td[7]/text()').extract()
            player_cont = d.xpath('td[@class="left"][2]/text()').extract()
            player_sal= d.xpath('td[@class="left"][2]/b/text()').extract()
            #print(player_img,player_cont)
            #item={}
            item ["playerimg"]=player_img[0] if player_img else ''
            item['playername'] = player_name[0] if player_name else ''
            item['playernumber'] =player_number[0] if player_number else ''
            item['playerjob'] = player_job[0] if player_job else ''
            item['playertall'] = player_tall[0] if player_tall else ''
            item['playerweight'] = player_weight[0] if player_weight else ''
            item['playerbirthday'] = player_birthday[0] if player_birthday else ''
            item['playercont'] = player_cont[0] if player_cont else 'NULL'
            item['playersal'] = player_sal[0] if player_sal else ''
            player_url = player_url[0] if player_url else ''
            print(player_url)
            
            yield item               
            #yield scrapy.Request(url=player_url, meta={'item': item}, 
            #                        callback=self.player_detail,dont_filter=True) 
        
    def player_detail(self, response):
         #for d in response.xpath('//table[@class="players_table bott"]//tr[not(@class)]'):
        pass
    
               
