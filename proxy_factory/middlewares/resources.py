#!/usr/bin/python
# -*- coding:utf8 -*-

"""
    @author:xiaotian zhao
    @time:12/22/18
"""

USER_AGENT_LIST = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"
]

PROXIES = [
    "124.205.155.153:9090",
    "119.90.126.106:7777",
    "223.85.196.75:9999",
    "123.139.56.238:9999",
    "123.139.56.238:9999",
    "222.221.11.119:3128",
    "221.7.255.168:80",
    "119.57.105.25:53281",
    "183.196.170.247:9000",
    "182.18.13.149:53281",
    "113.65.160.148:9797",
    "117.141.155.244:53281",
    "119.57.108.89:53281",
    "117.141.155.243:53281",
    "119.57.108.53:53281",
    "115.159.190.87:80",
    "175.102.3.98:8089",
    "163.125.157.97:8888",
    "163.125.73.149:9797",
    "218.66.253.146:8800",
    "101.89.132.131:80",
    "163.125.157.98:8888",
    "117.141.155.244:53281",
    "119.57.108.73:53281",
    "222.16.83.18:80",
    "124.237.83.14:53281",
    "101.231.50.154:8000",
    "183.196.168.194:9000",
    "163.125.72.218:9797",
    "163.125.156.253:8888",
    "124.205.155.157:9090",
    "123.139.56.238:9999",
    "123.139.56.238:9999",
    "222.132.145.122:53281",
    "183.196.168.194:9000",
    "183.195.145.174:53281",
    "180.76.111.69:3128",
    "119.57.109.129:53281",
    "101.89.132.131:80",
    "119.57.108.73:53281",
    "119.57.108.65:53281",
    "119.57.105.25:53281",
    "119.57.108.65:53281",
    "27.46.20.4:888",
    "124.205.155.157:9090",
    "124.207.82.166:8008",
    "222.217.19.248:8080",
    "117.141.155.243:53281",
    "124.205.155.156:9090",
    "111.11.98.58:9000",
    "119.57.108.65:53281",
    "124.205.155.158:9090",
    "183.196.168.194:9000",
    "119.57.108.73:53281",
    "223.85.196.75:9999",
    "60.5.254.169:8081",
    "119.57.108.53:53281",
    "101.231.50.154:8000",
    "183.195.145.174:53281",
    "222.217.19.248:8080",
    "163.125.18.185:8888",
    "112.115.57.20:3128",
    "119.57.108.89:53281",
    "124.205.155.158:9090",
    "113.65.160.148:9797",
    "112.91.218.21:9000",
    "218.22.7.62:53281",
    "183.196.170.247:9000",
    "163.125.18.182:8888",
    "163.125.18.180:8888",
    "119.90.126.106:7777",
    "113.200.214.164:9999",
    "119.57.108.89:53281",
    "119.57.108.65:53281",
    "115.159.190.87:80"
]
