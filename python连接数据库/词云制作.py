import jieba
import wordcloud
import imageio.v2 as imageio
mask=imageio.imread('心.jpg')
file_open=open('歌词评论.txt','r',encoding='utf-8')
txt=file_open.read()
words={}
Cloud=wordcloud.WordCloud(width=1000,height=1000,background_color='white',font_step=1,mask=mask,font_path='msyh.ttc',stopwords=words)
txtlist=jieba.lcut(txt)
string=''.join(txtlist)
Cloud.generate(string)
Cloud.to_file('词云.png')