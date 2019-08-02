# -*- coding: utf-8 -*-
import scrapy
from ..items import DangdangItem

class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/pg1-cid4004279.html']

    def parse(self, response):
        # 实例化对象
        item = DangdangItem()
        # 通过分析标签，我们可以依次得到相关的数据，并将它们赋值给item类中
        item["title"] = response.xpath("//a[@name='itemlist-title']/@title").extract()
        item["link"] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        print(item["title"],item["link"],item["comment"])
        # 提交数据，把数据传送给item类
        yield item
