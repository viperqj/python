from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
bro = webdriver.Chrome(service=s)
bro.get('https://www.taobao.com/')
#标签定位
search_input = bro.find_element(By.ID,'q')
#标签交互
search_input.send_keys('手机')

#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

btn = bro.find_element(By.XPATH,'//button[@class="btn-search tb-bg"]').click()
# 点击搜索按钮 btn.click()

bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()


sleep(5)
bro.quit()
