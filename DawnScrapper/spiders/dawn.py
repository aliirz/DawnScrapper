# -*- coding: utf-8 -*-
import scrapy
import delorean
from datetime import datetime

class DawnSpider(scrapy.Spider):
    name = "dawn"
    allowed_domains = ["dawn.com"]
    # start_urls = generate_urls()
    start_urls = (
        'http://www.dawn.com/newspaper/2015-01-07/',
        'http://www.dawn.com/newspaper/2015-03-03/',
        'http://www.dawn.com/newspaper/2015-02-05/'
    )

    def parse(self, response):
        # print response
        # check response for <h2> <a>
        # if contains tag 'election'
            # add to CSV

    def generate_urls():
        startDate = datetime(2012,05,12)
        endDate = datetime(2013, 05, 12)
        var urls = []
        for stop in stops(freq=delorean.DAILY, count = 10, timezone = 'US/Eastern', start = startDate, end = endDate):
            print stop

            # var url = 'http://www.dawn.com/newspaper/'
            # url = url + stop.str()
            # urls.add(url)
        # return urls



        # install delorean, python-dateutil, scrapy
