from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service("chromedriver.exe")
browser=webdriver.Chrome(service=s)
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
browser.get('https://www.bilibili.com/')
browser.maximize_window()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="i_cecream"]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span').click()
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/input').send_keys('18295841784')
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input').send_keys('qj123456')
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[3]/div[3]/div[2]').click()
time.sleep(1)
bz_png=browser.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[6]/div/div')
bz_png.screenshot('./bz.png')

import requests
from hashlib import md5
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
chaojiying = Chaojiying_Client('1564695819', 'qj20010222', '96001')	#用户中心>>软件ID 生成一个替换 96001
im = open('./bz.png', 'rb').read()
result=chaojiying.PostPic(im, 9004)['pic_str']
print(result)
all_list = []  # 要存储即将被点击的点的坐标  [[x1,y1],[x2,y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(browser).move_to_element_with_offset(bz_png, x, y).click().perform()
    time.sleep(0.5)
browser.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[6]/div/div/div[3]/a/div').click()
# time.sleep(20)

