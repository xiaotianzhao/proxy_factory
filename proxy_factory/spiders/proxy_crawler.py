#!/usr/bin/python
# -*- coding:utf8 -*-

"""
    @author:xiaotian zhao
    @time:12/24/18
"""

from __future__ import print_function
import scrapy

import re
import time
import random
import BeautifulSoup
from urllib import quote


class ProxyCrawler(scrapy.Spider):
    name = "proxy_crawler"
    allowed_domains = ['zhidao.baidu.com']
    start_urls = []

    def __init__(self, output_file_path=None, max_page_num=5):
        super(ProxyCrawler, self).__init__()
        self.max_page_num = int(max_page_num)
        self.output_file_path = output_file_path

        self.start_urls = [
            'https://www.kuaidaili.com/free/inha/{}/'.format(i) for i in range(self.max_page_num)
        ]

        if output_file_path:
            self.output_file = open(output_file_path, 'a')

    def parse(self, response):
        ips = response.xpath("//tr/td[1]/text()").extract()
        ports = response.xpath('//tr/td[2]/text()').extract()
        for ip, port in zip(ips, ports):
            if self.output_file_path:
                self.output_file.write('\"{}:{}\",\n'.format(ip, port))
            else:
                print("{}:{}".format(ip, port))
        time.sleep(random.randint(0, 2))
