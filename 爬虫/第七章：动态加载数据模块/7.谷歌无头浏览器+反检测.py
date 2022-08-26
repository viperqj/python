from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#实现无可视化界面(无头浏览器)
from selenium.webdriver import ChromeOptions
option=ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
s=Service("chromedriver.exe")
browser = webdriver.Chrome(service=s,options=option)
#规避检测
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
browser.get('https://www.taobao.com/')
print(browser.page_source)

