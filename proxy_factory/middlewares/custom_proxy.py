#!/usr/bin/python
# -*- coding:utf8 -*-

"""
    @author:xiaotian zhao
    @time:12/22/18
"""

from proxy_factory.middlewares.resources import PROXIES
import random


class RandomProxy(object):
    def process_request(self,request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = 'http://%s'% proxy