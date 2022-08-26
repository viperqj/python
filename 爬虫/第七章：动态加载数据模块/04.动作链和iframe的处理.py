from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#导入动作连
from selenium.webdriver import ActionChains
s=Service("chromedriver.exe")
bro=webdriver.Chrome(service=s)
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是存在于iframe标签之中的则必须通过如下操作进行标签定位
bro.switch_to.frame('iframeResult')#切换浏览器定位的作用域
div=bro.find_element(By.ID,'draggable')
#动作连实例化
action=ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)
for i in range(5):
    #perform()立即执行动作连操作
    #move_by_offset(17,0)x水平方向,y竖直方向
    action.move_by_offset(30,0).perform()
    sleep(0.3)
#释放动作链
action.release()
print(div)









