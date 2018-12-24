#!/usr/bin/python
# -*- coding:utf8 -*-

"""
    @author:xiaotian zhao
    @time:12/22/18
"""

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from proxy_factory.middlewares.resources import USER_AGENT_LIST


import random


class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers.setdefault('User-Agent', ua)
