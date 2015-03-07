# -*- coding: utf-8 -*-
import scrapy


class DawnSpider(scrapy.Spider):
    name = "dawn"
    allowed_domains = ["dawn.com"]
    start_urls = (
        'http://www.dawn.com/',
    )

    def parse(self, response):
        pass
