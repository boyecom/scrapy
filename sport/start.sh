#!/bin/bash
#describe:执行爬虫
#date:2019/09/27
#Author:lby

#/usr/local/python3/bin/scrapy crawl basketball
#/usr/local/python3/bin/scrapy crawl football
#/usr/local/python3/bin/scrapy crawl football_rank
#/usr/local/python3/bin/scrapy crawl football_score

hh=$(date +%H)
flag=0
while [ 1=1 ] ;do
    if [[ $hh -eq '22' || $hh -eq '8' ]] ;then
        echo "Time is $(date +%H:%M:%S)"
        if [ $flag -eq 0 ] ;then
            echo "running:/usr/local/python3/bin/scrapy crawl football_rank"
            /usr/local/python3/bin/scrapy crawl football_rank
            sleep 60
            echo "running:/usr/local/python3/bin/scrapy crawl football_score"
            /usr/local/python3/bin/scrapy crawl football_score
            flag=1 #爬取完成
            
        fi
    else
        sleep 1
        echo "sleep..."
    fi
    sleep 120
done

