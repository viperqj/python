import requests

#下载的视频是整个视频，不是需要拼接的那一种

# 传入下载的列表URL和文件的保存文件夹path 下载视频
def get_vi(url,path):
    # 获取网页的返回信息
    respons = requests.get(url).json()
    # 在响应里面获取需要的数据保存到列表
    vi_url = respons['data']['response']['videos']
    # 通过for循环把列表中的数据取出来并下载视频到本地
    for vi in vi_url:
        # 设置本地的文件保存
        path1 = path + vi['title'] + '.mp4'
        # 获取视频的下载链接
        vi = vi['play_url']
        # 访问链接
        vi = requests.get(vi).content
        # 把视频资源写入到指定的文件夹
        print(path1 + '下载中--------')
        with open(path1, 'wb') as mp4:
            mp4.write(vi)
        print(path1 + '下载完成')

# 需要下载视频的url列表
url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1626081142774'
# 下载的视频保存位置
path = './123'
# 调用下载视频的函数get_vi
a = get_vi(url,path)