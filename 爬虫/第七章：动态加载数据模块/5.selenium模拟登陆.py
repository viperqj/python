from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
word=eval(input("输入留言内容："))
word=str(word)
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
bro=webdriver.Chrome(service=s)
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag = bro.find_element(By.ID,"switcher_plogin")
a_tag.click()
userName_tag = bro.find_element(By.ID,'u')
password_tag =bro.find_element(By.ID,'p')
sleep(1)
userName_tag.send_keys('1564695819')
# userName_tag.send_keys('189334909')
sleep(1)
# password_tag.send_keys('qj109222')
password_tag.send_keys('qj20010222')
sleep(1)
btn = bro.find_element(By.ID,'login_button')
btn.click()
sleep(1)
# #滑块验证
# bro.switch_to.frame('tcaptcha_iframe')#切换浏览器定位的作用域
# div=bro.find_element(By.ID,'tcaptcha_drag_thumb')
# #动作连实例化
# action=ActionChains(bro)
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

bro.find_element(By.XPATH,'//*[@id="tab_menu_list"]/li[3]').click()
sleep(1)
# bro.find_element(By.XPATH,'//*[@id="fct_1564695819_403_2_1646704221_1_1"]/div[1]/div[4]/div[1]/a').click()
# sleep(1)
# bro.find_element(By.XPATH,'//*[@id="menuContainer"]/div/ul/li[4]/a').click()
# sleep(1)
# bro.find_element(By.XPATH,'//*[@id="friendship_promote_layer"]/table/tbody/tr[1]/td[2]/a').click()
#bro.switch_to.frame('veditor1_Iframe')
bro.find_element(By.XPATH,'//*[@id="menuContainer"]/div/ul/li[4]/a').click()
sleep(1)
bro.switch_to.frame('tgb')#他的id
bro.find_element(By.XPATH,'//*[@id="btnWantPost"]').click()
sleep(1)
bro.switch_to.frame('veditor1_Iframe')
ff=bro.find_element(By.XPATH,'/html/body')
ff.send_keys(word)
#退出一层iframe66666666666666666666666666666666666666666666666666666666666666
bro.switch_to.default_content()
bro.switch_to.frame('tgb')
dd=bro.find_element(By.XPATH,'//*[@id="btnPostMsg"]')
dd.click()
sleep(1)
bro.switch_to.default_content()
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')


