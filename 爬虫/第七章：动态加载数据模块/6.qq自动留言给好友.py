from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
# 请输入好友和留言内容
qq=input('输入QQ号：')
friend = input('请输入好友：')
word = input('请输入留言内容：')
# 创建一个模拟浏览器对象，然后通过对象去操作浏览器
option=ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
browser = webdriver.Chrome(service=s,options=option)
browser.get('https://qzone.qq.com/')
browser.maximize_window()
time.sleep(2)

browser.switch_to.frame('login_frame')
a_tag = browser.find_element(By.ID,"switcher_plogin")
a_tag.click()
userName_tag = browser.find_element(By.ID,'u')
password_tag =browser.find_element(By.ID,'p')
time.sleep(1)
userName_tag.send_keys(qq)
time.sleep(1)
password_tag.send_keys('自己的密码')
time.sleep(1)
btn = browser.find_element(By.ID,'login_button')
btn.click()

#滑块验证
# time.sleep(1)
# browser.switch_to.frame('tcaptcha_iframe')#切换浏览器定位的作用域
# div=browser.find_element(By.ID,'tcaptcha_drag_thumb')
# #动作连实例化
# action=ActionChains(browser)
# #点击长按指定的标签
# action.click_and_hold(div)
# for i in range(6):
#     #perform()立即执行动作连操作
#     #move_by_offset(17,0)x水平方向,y竖直方向
#     action.move_by_offset(28,0).perform()
#     sleep(0.3)
# #释放动作链
# action.release().perform()
# sleep(1)


browser.switch_to.default_content()  # 登陆完后回到默认框架
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="aMyFriends"]').click()
time.sleep(1)
element1 =browser.find_element(By.XPATH,'//*[@id="app_container"]/iframe')
browser.switch_to.frame(element1)
ff=browser.find_element(By.XPATH,'//*[@id="qz-search-box-input"]')
ff.send_keys(friend)
time.sleep(1)
browser.switch_to.default_content()
element2 =browser.find_element(By.XPATH,'//*[@id="app_container"]/iframe')
browser.switch_to.frame(element2)
browser.find_element(By.XPATH,'//*[@id="qz-search-box-result"]/li/div[2]/p').click()#难点
time.sleep(1)#搜索ok
browser.find_element(By.XPATH,'//*[@id="mecarewho_list"]/li/div[2]/div[2]/p/a').click()
time.sleep(1)#进入好友
# 获得打开的第一个窗口句柄
windows = browser.window_handles
browser.switch_to.window(windows[-1])
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="friendship_promote_layer"]/table/tbody/tr[1]/td[2]/a').click()
time.sleep(1)
#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.find_element(By.XPATH,'//*[@id="menuContainer"]/div/ul/li[4]').click()#或者  browser.find_element(By.XPATH,"//div[@id='layBackground']//li[@class = 'menu_item_334']//a[text()='留言板']").click()
time.sleep(3)#进入留言板
browser.switch_to.frame('tgb')
time.sleep(1)
browser.switch_to.frame('veditor1_Iframe')
time.sleep(1)
ff=browser.find_element(By.XPATH,'/html/body')#留言框
ff.send_keys(word)
browser.switch_to.default_content()
browser.switch_to.frame('tgb')
dd=browser.find_element(By.XPATH,'//*[@id="btnPostMsg"]')
dd.click()#确认发表按钮
print("留言成功！！！")
time.sleep(2)
browser.quit()




