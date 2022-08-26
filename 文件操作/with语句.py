# with语句可以自动管理上下文资源,不论什么原因跳出with都能确保文件正确的关闭，以此来达到释放资源的目的
with open('./a.txt','w+',encoding='utf-8') as fp:
    fp.write('努力学习')