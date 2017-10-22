# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 15:26
# @Author  : Mrxn
# @File    : douban_spider.py
# @Software: PyCharm
# @Desc     :The DeFault DeSc for Mrxn
# @license : Copyright(C), Mrxn
# @Contact : admin@mrxn.net
# @Blog    : https://mrxn.net

from scrapy import Request
from scrapy.spiders import Spider
from doubanmovietop250.items import Doubanmovietop250Item

class DoubanMovieTop250ISpider(Spider):
    name = 'douban_movie_top250'
    # 设置header不然不能打开豆瓣的
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url,headers=self.headers)

    # ---------------------------------爬取模块------------------------------------#
    def parse(self, response):
        item = Doubanmovietop250Item()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
            yield item
        # ---------------------------------自动翻页------------------------------------#
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)