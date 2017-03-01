#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import scrapy
import re
import HTMLParser
from scrapy.selector import HtmlXPathSelector


# @author: UUTAN (uutan@qq.com)
# 1 获取国家,LOGO
# 2 获取各个国家的赛事
#
class countySpider(scrapy.spiders.Spider):
    name = 'county'
    allowed_domain = ["info.sporttery.cn"]
    start_urls = [
        "http://info.sporttery.cn/football/history/data_center.php"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        sites = hxs.select('//div[@class="matchList"]')
        # print sites

        # 国家列表
        for site in sites:
            image = site.select('div/a/img/@src').extract()
            title = site.select('div[@class="match-name"]/div/text()').extract()
            print title,image
            
            # 赛事列表
            matchs  = site.select('div/ul/li')
            for match in matchs:
                mid = match.select('a/@href').extract() # TODO 需要使用re(r'正则')过滤出数字
                match_name = match.select('a/text()').extract()
                print mid,match_name