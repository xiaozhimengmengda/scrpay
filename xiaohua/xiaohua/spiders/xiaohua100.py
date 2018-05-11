# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import XiaohuaItem
from scrapy.http import Request


class Xiaohua100Spider(scrapy.Spider):
    name = 'xiaohua100'
    allowed_domains = ['xiaohua100.cn']
    start_urls = ['http://www.xiaohua100.cn/plus/waterfall.php?tid=1&sort=lastpost&totalresult=890&pageno={}&r=0.8261354727827863&display=pic&isAjax=1&l=1358747256127773&ts=135874808804&tk=cb50cab524b3be07ac28fc6141350f86']
    n = 0

    def parse(self, response):
        hsx1 = Selector(response=response).xpath("//div[@data-uid='1']")

        for obj in hsx1:
            host_urls = 'http://www.xiaohua100.cn'
            images = obj.xpath(".//div[@class='pic']")
            image_url = images.xpath(".//a/img/@src").extract_first().strip()
            titles = obj.xpath(".//span[@class='cellTit']/a/text()").extract_first().strip()
            vote = obj.xpath(".//a[@class='praise-num']/text()").extract_first().strip()
            image_urls = f'{host_urls}{image_url}'
            yield XiaohuaItem(image_urls=[image_urls], titles=titles)

        for x in range(1, 13):
            url = self.start_urls[0].format(x)
            yield Request(url=url, callback=self.parse)
