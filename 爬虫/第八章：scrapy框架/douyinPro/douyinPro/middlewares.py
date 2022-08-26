# - 下载中间件
#         - 位置：引擎和下载器之间
#         - 作用：批量拦截到整个工程中所有的请求和响应
#         - 拦截请求：
#             - UA伪装:process_request
#             - 代理IP:process_exception:return request
#
#         - 拦截响应：
#             - 篡改响应数据，响应对象

from scrapy import signals
import os
import re
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
from selenium.webdriver.common.by import By
from time import sleep
from scrapy.http import HtmlResponse
class DouyinproDownloaderMiddleware:
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
        '125.106.138.41:4234',
        '42.6.114.117:7018',
    ]
    PROXY_https = [
        '110.89.123.129:4213',
        '118.123.40.30:4231',
    ]

    # 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        request.headers['User-Agent'] = random.choice(self.user_agent_list)

        return None

    def process_response(self, request, response, spider):
        if request.url  not in spider.douyin_urls:
            bro = spider.bro
            bro.get(request.url)
            sleep(1)
            try:
                bro.find_element(By.XPATH, '//*[@id="login-pannel"]/div[2]').click()
            except:
                bro.find_element(By.XPATH, '//*[@id="verify-bar-close"]').click()
                bro.find_element(By.XPATH, '//*[@id="login-pannel"]/div[2]').click()
            aa = bro.find_element(By.XPATH,
                                  '//*[@id="douyin-header"]/div/header/div/div/div[1]/div/div[2]/div/div[1]/form/input[1]')
            aa.send_keys(spider.word)
            sleep(1)
            bro.find_element(By.XPATH,
                             '//*[@id="douyin-header"]/div/header/div/div/div[1]/div/div[2]/div/div[1]/button').click()
            sleep(1)
            windows = bro.window_handles
            bro.switch_to.window(windows[-1])
            sleep(1)
            bro.find_element(By.XPATH, '//*[@id="dark"]/div[2]/div/div[1]/div/div/span[3]').click()
            sleep(1)
            bro.find_element(By.XPATH, '//*[@id="dark"]/div[2]/div/div[3]/div[3]/ul/li[1]/div/a/div[1]/div[2]/div[1]/p/span/span/span/span/span').click()
            windows = bro.window_handles
            bro.switch_to.window(windows[-1])
            sleep(1)
            #如果目标用户作品数量多 请使用此循环 因为数据是随着滚动条加载的
            for i in range(0, 3):
                bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                sleep(1)
            sleep(1)
            # bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            bb = bro.page_source
            url=bro.current_url
            new_response = HtmlResponse(url=url, body=bb, encoding='utf-8', request=request)
            return new_response
        else:
            bro = spider.bro
            bro.get(request.url)
            sleep(2)
            page_text = bro.page_source
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response

    def process_exception(self, request, exception, spider):
        # 拦截发生异常的请求
        if request.url.split(':')[0] == 'http':
            # 代理
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)

        return request  # 将修正之后的请求对象进行重新的请求发送



