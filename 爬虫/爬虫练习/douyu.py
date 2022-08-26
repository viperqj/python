import json
import requests
import datetime
from queue import Queue
import threading


class DouyuTVSpider:
    def __init__(self):
        self.base_url = "https://www.douyu.com/gapi/rkc/directory/0_0/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        self.url_queue = Queue()
        self.parse_queue = Queue()
        self.write_queue = Queue()
        self.thread_list = []

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            response_data = response.content.decode()
            self.parse_queue.put(response_data)
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            str_data = self.parse_queue.get()
            json_data = json.loads(str_data)
            live_list = json_data['data']['rl']
            need_list =[]
            for x in live_list:
                need_dict = {key: value for key, value in x.items() if
                             key in ["rs16", "nn", "ol", "c2name", "rn"]}
                need_dict["spider_time"] = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
                need_list.append(need_dict)
            self.write_queue.put(need_list)
            self.parse_queue.task_done()

    def save_content_list(self):
        while True:
            data = self.write_queue.get()
            with open("douyuTV-update.json",'a',encoding='utf-8') as f:
                f.write(json.dumps(data,ensure_ascii=False,indent=4)+",")
            self.write_queue.task_done()

    def run(self):
        with open("douyuTV-update.json", 'a', encoding='utf-8') as f:
            f.write('{"data":[')
        for x in range(1, 51):
            self.url_queue.put(self.base_url + f"{x}")
        for x in range(2):
            t_url = threading.Thread(target=self.parse_url)
            self.thread_list.append(t_url)
        for x in range(3):
            t_content = threading.Thread(target=self.get_content_list)
            self.thread_list.append(t_content)
        for x in range(4):
            t_write = threading.Thread(target=self.save_content_list)
            self.thread_list.append(t_write)
        for t in self.thread_list:
            t.setDaemon(True)
            t.start()
        for q in [self.url_queue,self.parse_queue,self.write_queue]:
            q.join()
        with open("douyuTV-update.json", 'rb+') as f:
            f.seek(0, 2)  # end of file
            size = f.tell()  # the size...
            f.truncate(size - 1)
        with open("douyuTV-update.json", 'a', encoding='utf-8') as f:
            f.write("]}")


if __name__ == "__main__":
    douyuTV_spider = DouyuTVSpider()
    douyuTV_spider.run()

