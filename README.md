# Proxy Factory
Http代理爬虫
### Environment
- python2.x
- scrapy
- argparse
### Run
- 进入根目录，scrapy crawl proxy_crawler -a output_file_path=proxies.txt -a max_page_num=5
- python test_proxy.py --source_proxy_file=proxies.txt --available_proxy_file=available_proxies.txt
