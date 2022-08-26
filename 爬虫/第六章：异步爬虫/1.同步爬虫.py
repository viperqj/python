import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
urls = [
    'https://pic.netbian.com/uploads/allimg/210920/165135-16321278956369.jpg',
    'https://pic.netbian.com/uploads/allimg/220131/012219-1643563339f065.jpg',
    'https://pic.netbian.com/uploads/allimg/220218/003619-164511577931be.jpg'
]

def get_content(url):
    print('正在爬取：',url)
    #get方法是一个阻塞的方法
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200 :
        return response.content

def parse_content(content):
    print('响应数据的长度为：',len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)