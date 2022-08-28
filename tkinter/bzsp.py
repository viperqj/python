import subprocess
import requests
import re
import json
class BzSpider():
    def __init__(self):
        self.url = 'https://www.bilibili.com/video/%s?'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25',
            'referer': 'https://www.bilibili.com/'
        }
    def send_request(self,url):
        res=requests.get(url=url,headers=self.headers).text
        self.parse_html(res)
    def parse_html(self, res):
        title=re.findall('<h1 title="(.*?)"',res)[0]
        # re.sub()替换
        title=re.sub(r'[\/:?*|,.<>"]','',title)
        html_data=json.loads(re.findall('<script>window.__playinfo__=(.*?)</script>',res)[0])
        audio_url=html_data['data']['dash']['audio'][0]['backupUrl']
        video_url=html_data['data']['dash']['video'][0]['backupUrl']
        if str(audio_url)=='None' or str(video_url)=='None':
            print('获取失败，正在重新获取...')
            self.start()
        else:
            audio_content=requests.get(url=audio_url[0],headers=self.headers).content
            video_content=requests.get(url=video_url[0],headers=self.headers).content
            self.save(audio_content,video_content,title)
    def save(self,audio_content,video_content,title):
        with open(title+'.mp3','wb') as fp:
            fp.write(audio_content)
        with open(title+'.mp4','wb') as fp:
            fp.write(video_content)
        print('下载成功')
        cmd=f'ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental {title}output.mp4'
        subprocess.run(cmd,shell=True)
        print('视频合成成功')
    def start(self,name):
        url = self.url % name
        self.send_request(url)
if __name__ == '__main__':
    bz=BzSpider()
    bz.start()
