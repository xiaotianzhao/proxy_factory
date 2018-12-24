#!/usr/bin/python
# -*- coding:utf8 -*-

"""
    @author:xiaotian zhao
    @time:12/24/18
"""

import codecs
import argparse
import requests

def is_success(proxy):
    try:
        requests.get('https://www.sogou.com/', proxies={"http":"http://{}".format(proxy)}, timeout=3)
    except Exception as e:
        print(e)
        return False
    else:
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_proxy_file', default='proxies.txt', type=str)
    parser.add_argument('--available_proxy_file', default='available_proxies.txt', type=str)

    args = parser.parse_args()
    target_file = codecs.open(args.available_proxy_file, 'w', encoding='utf8')

    proxies = []
    with codecs.open(args.source_proxy_file, 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            line = line[:-1]
            if is_success(line):
                target_file.write('{},\n'.format(line))
                print('{}, success'.format(line))
            else:
                print('{}, failed'.format(line))


