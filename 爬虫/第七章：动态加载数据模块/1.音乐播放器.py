from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
name=input("输入想听的歌曲名字：")
option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=option)
driver.get('http://tool.liumingye.cn/music/?page=searchPage')
aa=driver.find_element(By.XPATH,'//*[@id="input"]')
aa.send_keys(name)
driver.find_element(By.XPATH,'//*[@id="search"]/div[2]/div/button[2]').click()

