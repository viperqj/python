from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from lxml import etree

aa = input('出发地址:')
bb = input('目的地:')
cc = input('出发日期（注意格式例如 2022-03-28）:')
# 无头浏览器
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
# browser = webdriver.Chrome(service=s, options=option)
browser = webdriver.Chrome(service=s)
# 规避检测
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
browser.get('https://user.qunar.com/passport/login.jsp?ret=https%3A%2F%2Fwww.qunar.com%2F%3Fex_track%3Dauto_4e0d874a')
browser.maximize_window()
sleep(1)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]').click()
sleep(1)
username = browser.find_element(By.ID, 'username')
password = browser.find_element(By.ID, 'password')
sleep(1)
username.send_keys('16635428653')
sleep(1)
password.send_keys('qj20010222')
sleep(1)
browser.find_element(By.XPATH, '//*[@id="agreement"]').click()
sleep(1)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[3]').click()
sleep(1)
huakuai = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[5]/div/div/div[3]/div[3]')
huakuai_left_right = huakuai.location
huakuai_height_widtht = huakuai.size
# print(huakuai_left_right,huakuai_height_widtht)
guidao = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[5]/div/div/div[3]/div[2]')
guidao_left_rihgt = guidao.location
guigao_height_widtht = guidao.size
# print(guidao_left_rihgt,guigao_height_widtht)
length = guigao_height_widtht['width'] - huakuai_height_widtht['width']
# 动作连实例化,破解滑块验证码
action = ActionChains(browser)
# 点击长按指定的标签
action.click_and_hold(huakuai)
action.move_by_offset(length + 2, 0).perform()
# perform()立即执行动作连操作
# 释放动作链
action.release().perform()
sleep(1)
browser.find_element(By.XPATH, '//*[@id="js_nva_cgy"]/li[3]/a').click()
sleep(2)
browser.find_element(By.XPATH, '//*[@id="js-con"]/div[1]/form/div[1]/div[1]/div[1]/div/div/input').send_keys(aa)
sleep(1)
browser.find_element(By.XPATH,
                     '//*[@id="js-con"]/div[1]/form/div[1]/div[1]/div[1]/div/div/div[5]/div/table/tbody/tr[1]').click()
sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-con"]/div[1]/form/div[1]/div[1]/div[2]/div/div/input').send_keys(bb)
sleep(1)
browser.find_element(By.XPATH,
                     '//*[@id="js-con"]/div[1]/form/div[1]/div[1]/div[2]/div/div/div[5]/div/table/tbody/tr[1]').click()
sleep(1)
ff = browser.find_element(By.XPATH, '//*[@id="js-con"]/div[1]/form/div[1]/div[2]/div/div/div[1]/input')
for i in range(10):
    ff.send_keys(Keys.BACK_SPACE)
ff.send_keys(cc)
ff.click()
sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-con"]/div[1]/form/div[2]/div/span/button').click()
sleep(1)
page = browser.page_source
tree = etree.HTML(page)
li = tree.xpath('//*[@id="list_listInfo"]/ul[2]/li')
n = 0
fp = open('./火车票数据', 'w', encoding='utf-8')
for i in li:
    n = n + 1
    all_data = []
    c = i.xpath('.//div/div[1]/h3/text()')
    all_data.append(c[0])
    l = i.xpath('.//div/div[3]/time[1]/text()')
    all_data.append(l[0])
    d = i.xpath('.//div/div[4]/time/text()')
    all_data.append(d[0])
    all_data = str(all_data)
    fp.write(all_data + '\n')
    print("第{}趟列车{} 出发时间为{} 运行时间为{}".format(n, c[0], l[0], d[0]))
browser.save_screenshot('./火车票.png')