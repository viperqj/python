# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random
from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware(object):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    PROXY_http = [
        '42.56.238.53:4256',
        '121.61.206.28:4231',
    ]
    PROXY_https = [
        '49.83.195.21:4232',
        '42.6.114.121:3897',
    ]


# 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        request.headers['User-Agent'] = random.choice(self.user_agent_list)

        return None

    #该方法拦截四大板块对应的响应对象，进行篡改
    def process_response(self, request, response, spider):#spider爬虫对象
        bro = spider.bro#获取了在爬虫类中定义的浏览器对象

        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        if request.url in spider.models_urls:
            bro.get(request.url) #四个板块对应的url进行请求
            sleep(3)
            page_text = bro.page_source  #包含了动态加载的新闻数据

            #response #四大板块对应的响应对象
            #针对定位到的这些response进行篡改
            #实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来旧的响应对象
            #如何获取动态加载出的新闻数据？
                #基于selenium便捷的获取动态加载数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)

            return new_response
        else:
            #response #其他请求对应的响应对象
            return response





    def process_exception(self, request, exception, spider):
        # 拦截发生异常的请求
        def process_exception(self, request, exception, spider):
            if request.url.split(':')[0] == 'http':
                # 代理
                request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
            else:
                request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)

            return request  # 将修正之后的请求对象进行重新的请求发送
