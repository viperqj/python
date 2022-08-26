import requests
from lxml import etree
from hashlib import md5

def getText(imgpath):
    class Chaojiying_Client(object):
        def __init__(self, username, password, soft_id):
            self.username = username
            password =  password.encode('utf8')
            self.password = md5(password).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }

        def PostPic(self, im, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
            }
            params.update(self.base_params)
            files = {'userfile': ('ccc.jpg', im)}
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
            return r.json()

        def ReportError(self, im_id):
            """
            im_id:报错题目的图片ID
            """
            params = {
                'id': im_id,
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
            return r.json()

    chaojiying = Chaojiying_Client('1564695819', 'qj20010222', '96001')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgpath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, 1902)


url='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
session = requests.Session()
page_text=session.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
img_src='http://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data=session.get(url=img_src,headers=headers).content
with open('./yz.jpg','wb')as fp:
    fp.write(img_data)
result=getText('yz.jpg')
code=result["pic_str"]
print(code)
VIEWSTATE=tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
data={
'__VIEWSTATE': VIEWSTATE,
'__VIEWSTATEGENERATOR':' C93BE1AE',
'from':' http://so.gushiwen.cn/user/collect.aspx',
'email':' 18295841784',
'pwd':' qj20010222',
'code': code,
'denglu':' 登录'
}
response=session.post(url=url,data=data,headers=headers)
print(response.status_code)
'''login_page_text=session.post(url=url,data=data,headers=headers).text
with open('./gushi.html','w',encoding='utf-8')as fp:
    fp.write(login_page_text)'''






