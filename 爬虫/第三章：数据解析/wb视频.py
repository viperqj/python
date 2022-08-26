import requests
import os
k=0
# if not os.path.exists('.wb/短视频'):
#     os.mkdir('./wb短视频')
url='https://weibo.com/tv/api/component?page=%2Ftv%2Fchannel%2F4379160563414111%2Feditor'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
'referer': 'https://weibo.com/tv/channel/4379160563414111/editor',
'cookie': 'SUB=_2AkMVNrSEf8NxqwJRmPgRzWvhao5wzgnEieKjakVfJRMxHRl-yT8XqnUAtRB6PraabkVLdwRjQ5qMcVWf2wLILffJa_kA; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gO.lh1JoATTsT816Xz7yZ; SINAGLOBAL=522969198490.6615.1651129427661; WBPSESS=dby_ax9VEUsyOWBxkfTkWgF2kq0xMN0rtXq04y8qpgdssP0y7IqoHplmh3WSwQBC-hAegnk8CoJeGWdrSmUamv5VH7_gpnudWxsnjCcX53IYdTH3Jj-olA0U2mvGrwKGjj1B3e_IRpthMcq3FavO5FsKbSxh1ytmpefJhjZd5gk=; _s_tentry=weibo.com; Apache=4433771038804.157.1651489589160; ULV=1651489589265:7:2:2:4433771038804.157.1651489589160:1651489184762; XSRF-TOKEN=LiLAZl5pFbyANJNkFnvD7oQi; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0'
}
data={'data': '{"Component_Channel_Editor":{"next_cursor":4763347493781538,"cid":"4379160563414111","count":9}}'}
response=requests.post(url=url,data=data,headers=headers).json()
data_list=response['data']['Component_Channel_Editor']
next_cursor=str(data_list['next_cursor'])
for i in data_list['list']:
    oid = i['oid']
    src = 'https://weibo.com/tv/api/component?page=%2Ftv%2Fshow%2F1034%3A' + oid[5:]
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
        'referer': 'https://h5.video.weibo.com/show/' + oid,
        'Cookie': 'SUB=_2AkMVNrSEf8NxqwJRmPgRzWvhao5wzgnEieKjakVfJRMxHRl-yT8XqnUAtRB6PraabkVLdwRjQ5qMcVWf2wLILffJa_kA; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gO.lh1JoATTsT816Xz7yZ; SINAGLOBAL=522969198490.6615.1651129427661; WBPSESS=dby_ax9VEUsyOWBxkfTkWgF2kq0xMN0rtXq04y8qpgdssP0y7IqoHplmh3WSwQBC-hAegnk8CoJeGWdrSmUamv5VH7_gpnudWxsnjCcX53IYdTH3Jj-olA0U2mvGrwKGjj1B3e_IRpthMcq3FavO5FsKbSxh1ytmpefJhjZd5gk=; _s_tentry=weibo.com; Apache=4433771038804.157.1651489589160; ULV=1651489589265:7:2:2:4433771038804.157.1651489589160:1651489184762; XSRF-TOKEN=LiLAZl5pFbyANJNkFnvD7oQi; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0'
    }
    da = {'data': '{"Component_Play_Playinfo":{"oid":"1034:4763306590928936"}}'}
    da['data'] = da['data'].replace('1034:4763306590928936', oid)
    responses = requests.post(url=src, data=da, headers=header).json()
    aa = responses['data']['Component_Play_Playinfo']
    if len(str(aa)) < 50:
        print('违规视频已跳过')
    else:
        dict_url = aa['urls']
        title = responses['data']['Component_Play_Playinfo']['title']
        for i in dict_url:
            urll = 'https:' + dict_url[i]
            break
        # head = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
        # content = requests.get(url=urll, headers=head).content
        # imgPath = './wb短视频/' + title + '.mp4'
        # with open(imgPath, 'wb') as fp:
        #     fp.write(content)
        k=k+1
        print(title + '下载完成下载地址为',urll)

def qj(next_cursor):
    data['data'] = list(data['data'])
    data['data'][43:59] = next_cursor
    data['data'] = ''.join(data['data'])
    response=requests.post(url=url,data=data,headers=headers).json()
    data_list=response['data']['Component_Channel_Editor']
    next_cursor=str(data_list['next_cursor'])
    for i in data_list['list']:
        oid = i['oid']
        src = 'https://weibo.com/tv/api/component?page=%2Ftv%2Fshow%2F1034%3A' + oid[5:]
        # header = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
        #     'referer': 'https://h5.video.weibo.com/show/' + oid,
        #     'Cookie': 'SINAGLOBAL=5088490525489.586.1618059192687; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhVxYLR8Z-ac5jBVm6ay6Cb5JpX5KMhUgL.Fo-4e0qc1KqRS0M2dJLoIEnLxK-LBKBLBK.LxKMLBK.LB.2LxKBLBo.L12zLxK-LBKBL1Kqpeh2N; UOR=www.baidu.com,weibo.com,login.sina.com.cn; SCF=AtvKsDMPLhVz8L0IJjgfpV5NEcnBZddfwKLBQb0CWAwgcsSGd7o50MESIzyLGh4SLPHMUbHVw9ERl7R3ZB_mKZ8.; ALF=1682674933; SUB=_2AkMVNu62dcPxrAZYm_4TxW3qa4pH-jym44dAAn7uJhMyAxgP7mkOqSVutBF-XEegB2ZsfL8mdIdjROWw31-DmMi7; _s_tentry=weibo.com; Apache=128516381472.5787.1651139321571; ULV=1651139321698:12:7:7:128516381472.5787.1651139321571:1651138961093; YF-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230'
        # }
        da = {'data': '{"Component_Play_Playinfo":{"oid":"1034:4763306590928936"}}'}
        da['data'] = da['data'].replace('1034:4763306590928936', oid)
        responses = requests.post(url=src, data=da, headers=header).json()
        aa=responses['data']['Component_Play_Playinfo']
        if len(str(aa))<50:
            print('违规视频已跳过')
        else:
            dict_url = aa['urls']
            title=responses['data']['Component_Play_Playinfo']['title']
            for i in dict_url:
                urlll = 'https:' + dict_url[i]
                break
            # head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
            # content=requests.get(url=urlll,headers=head).content
            # imgPath = './wb短视频/' + title + '.mp4'
            # with open(imgPath, 'wb') as fp:
            #     fp.write(content)
            global k
            k=k+1
            print(title+'下载完成下载地址为',urlll)
            print('已抓取',k,'个视频')
    qj(next_cursor)
qj(next_cursor)