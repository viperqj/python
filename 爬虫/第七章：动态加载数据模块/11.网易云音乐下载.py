# coding=utf-8
from Crypto.Cipher import AES
import base64
import codecs
import random
import requests
import math
import json
import re


class WangyiyunDownload(object):
    def __init__(self):
        # "爱心", "女孩", "惊恐", "大笑"的值
        # 对应的js --> bqL0x(["爱心", "女孩", "惊恐", "大笑"])
        self.key = '0CoJUm6Qyw8W8jud'
        # "流泪", "强"的值
        # 对应的js --> bqL0x(["流泪", "强"])
        self.public_key = "010001"
        # 一串表情的值(省略,对应的js --> Yb5g.md)
        # 对应的js --> bqL0x(Yb5g.md)
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        # 偏移量
        self.iv = "0102030405060708"
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            # 这里需传入登录cookie,并且必须是会员账户才能访问会员曲目,否则只能访问免费曲目
            'Cookie': 'MUSIC_A_T=1501500688671; MUSIC_R_T=1501500776463; _ntes_nuid=3f10e64fadfb0e0cc2b141a40c1e13cb; NMTID=00O_PjkPOCOnxD1V0RSu7bDUITAmm8AAAF2uWhT-A; WM_TID=KWTu%2FhvBDgJFFUFBBFY%2FLJrGPZQjhoIq; WEVNSM=1.0.0; WNMCID=qtkekj.1634111899514.01.0; _ntes_nnid=3f10e64fadfb0e0cc2b141a40c1e13cb,1643033124801; UM_distinctid=17f150bfe0229-03fd84264dba08-50684351-144000-17f150bfe034c; vinfo_n_f_l_n3=f6dccb7d35cee818.1.0.1649424302291.0.1649425380031; WM_NI=jfUN4ruVnaJf%2BA3i6Ntt3jr2vWKMLDkvPmELeSw0kGeCRp0AXH4SlDhfo96daw9ouXBd5Z6nraNiHany9koQZVMLZRdwGawh9%2B7mcnKjlwU2O3EEO1HOgPyFL5LuDKEJS2s%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee99f67ab49fa2b5f75094b48bb3c14a828b9e83c55b8c91ba98f060949e8b85f62af0fea7c3b92aaaba9bafb77ab78aa282c96ee99ffd8ab546b8acfd8bf13ab68985aecf50a9aaa08ec848a78db9d1ea4da79d9e91b34b9c98fcb4ef50acbaa1dab570a3a9f790f85482bcfbbbb566b2bf828acb6baea7f78cee5b9a8a83add95aa8a98982f664fbf5f98ee26689b6a498d83a8ded8ba6ce3b8c91a9b1fc4e90eb8496c74187969dd3f237e2a3; ntes_kaola_ad=1; __remember_me=true; playerid=20001162; _iuqxldmzr_=33; JSESSIONID-WYYY=GQQXHSYdVDtoj1ibxKo%5CuA3IbBjqJtzhg9HpWiJId4QR%2Bx3bRMjOKtCgJC7E%5Colt%2Bm%5Ce9P7dX0F1CFnd8pYGh%2FxAWcxXNzMn04dxoh78frITi%5CDhBXOXZ1nwHfkYE6qp5VregI%2BN2XAuSc%5CmdKbSrNwWfx9SHBhvC8QW09SppsWcUCvq%3A1650878190662; MUSIC_U=1667ad21f6f93a10f070badee41f4a078ad3b565c0261080bfb5e3fe638cae6aef81e6984ce9c6ac0864666d348fe173388c250d54fc251e404df88cdb2565ce2538c30c63d58a6e58323a99dde6a555fbac7a3963f1d84c111109be15a0099e090f3ad7c86ad1db; __csrf=15a38d6cb7b6e7c7d5bd0a86bfbdbe13',
        }
        # 请求url
        self.url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

    # 生成16位随机数字符串
    # 对应的js --> a函数
    def set_random_num(self):
        random_num = ''
        # 从此字符串随机取出16个字符
        string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in range(16):
            # random.uniform(0, 1) * len(string): 生成一个实数,范围在0 <= n < len(string)
            # math.floor(n): 将n向下取整
            n = math.floor(random.uniform(0, 1) * len(string))
            # 从string中取出下标为n的字符拼接到random_num中
            random_num += string[n]
        print('已生成16位随机字符串!')
        # 返回16位随机数字符串
        return random_num

    # 生成encSecKey
    # 对应的js --> c函数
    # 通过public_key和modulus对random_num进行RSA加密
    # random_num: 生成的16位随机数字符串
    def RSA_encrypt(self, random_num):
        # 先将16位随机数字符串倒序并以utf-8编码
        random_num = random_num[::-1].encode('utf-8')
        # 然后再将其以hex(16进制)编码
        random_num = codecs.encode(random_num, 'hex_codec')
        # 加密(三者均要从16进制转换为10进制)
        # int(n, 16) --> 将16进制字符串n转换为10进制
        encryption = int(random_num, 16) ** int(self.public_key, 16) % int(self.modulus, 16)
        # 将加密后的数据转换为16进制字符串
        encryption = format(encryption, 'x')
        # 返回加密后的字符串
        return encryption

    # 生成params
    # 对应的js --> b函数
    # 根据key和iv对msg进行AES加密,需调用两次
    # key:
    #   第一次: key
    #   第二次: random_num
    # iv: 偏移量iv
    def AES_encrypt(self, msg, key, iv):
        # 先将msg按需补全至16的倍数
        # 需补全的位数
        pad = (16 - len(msg) % 16)
        # 补全
        msg = msg + pad * chr(pad)
        # 这里需要将key,iv和msg均以utf-8编码
        key = key.encode('utf-8')
        iv = iv.encode('utf-8')
        msg = msg.encode('utf-8')
        # 根据key和iv生成密钥,模式为CBC模式
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        # 加密
        encrypt_aes = encryptor.encrypt(msg)
        # 先将加密后的值进行base64编码
        encrypt_text = base64.encodebytes(encrypt_aes)
        # 再将其转换为utf-8字符串
        encrypt_text = str(encrypt_text, 'utf-8')
        # 返回加密后的字符串
        return encrypt_text

    # 根据歌曲song_id,生成需要传输的data
    # 其中包括params和encSecKey
    def construct_data(self, song_id):
        # 先生成16位随机数字符串
        random_num = self.set_random_num()
        # 生成encSecKey
        encSecKey = self.RSA_encrypt(random_num=random_num)
        print('已生成encSecKey!')
        # 调用两次AES加密生成params
        # 先初始化歌曲song_info
        song_info = '{"ids":"[%s]","level":"standard","encodeType":"aac","csrf_token":"477c1bd99fddedb3adc074f47fee2d35"}' % song_id
        # 第一次加密,传入encText, key和iv
        first_encryption = self.AES_encrypt(msg=song_info, key=self.key, iv=self.iv)
        # 第二次加密, 传入first_encryption, random_num和iv
        encText = self.AES_encrypt(msg=first_encryption, key=random_num, iv=self.iv)
        print('已生成encText!')
        # 生成data
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        # 返回data
        return data

    # 发送请求,获取下载链接
    def get_real_url(self):
        # 输入歌曲song_id
        self.song_id = input('请输入歌曲id:')
        # 获取data
        data = self.construct_data(song_id=self.song_id)
        print('正在发送请求......')
        # 发送请求
        request = requests.post(url=self.url, headers=self.headers, data=data)
        # 初始化real_url
        real_url = ''
        # 处理返回信息
        try:
            js_text = json.loads(request.text)
            data = js_text['data']
            if len(data) != 0:
                code = data[0]['code']
                # 获取成功
                if code == 200:
                    # 歌曲真实地址
                    real_url = data[0]['url']
                    print('下载链接: %s' % real_url)
                # 会员歌曲,cookie过期，无法下载
                elif code == -110:
                    print('这是会员歌曲,而会员账户cookie已过期!')
                # 未搜索到歌曲
                elif code == 404:
                    print('输入的歌曲id有误!')
                else:
                    print('未知错误!')
        except:
            print('生成的params和encSecKey有误!可重试!')
        # 返回real_url
        return real_url

    def download(self):
        # 获取下载链接
        real_url = self.get_real_url()
        if real_url == '':
            print('链接获取失败!')
        else:
            # 获取歌曲名和歌手名
            url = 'https://music.163.com/song?id=%s' % self.song_id
            text = requests.get(url=url, headers=self.headers).text
            pattern = re.compile(r'歌曲名《(.*?)》.*?由 (.*?) 演唱.*?')
            song = pattern.findall(text)[0][0]
            print('歌曲名: %s' % song)
            singer = pattern.findall(text)[0][1]
            print('歌手名: %s' % singer)
            # 拼接文件名
            file = '{}-{}.mp3'.format(singer, song)
            # 开始下载
            print('正在下载......')
            content = requests.get(url=real_url, headers=self.headers).content
            with open(file, 'wb') as fp:
                fp.write(content)
            print('下载成功!')


if __name__ == '__main__':
    WangyiyunDownload().download()
