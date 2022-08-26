import csv
def demo1():
    fp=open(r"C:\Users\xiaoxin15\Desktop\太谷美食商家数据.csv",'rt')
    for i in fp:
        b = []
        i=i.replace('https','http')
        b.append(i)
        for n in b:
            c=''.join(n)
            print(c,end='')
    fp.close()
def demo2():
    fp=open(r'E:\bzpachong\第七章：动态加载数据模块\火车票数据',encoding='utf-8')
    f = open('./hcp.csv', 'w+', encoding='utf-8',newline='' )
    csv_write = csv.DictWriter(f, fieldnames=[
        '车次',
        '发车时间',
        '运行时间',
    ])
    csv_write.writeheader()
    a=[]
    for i in fp:
        i=i.replace(' ','')
        i = i.replace(r'\n','')
        i = i.replace('[', '')
        i=i.replace(']', '')
        i = i.replace('\n', '')
        a=''.join(i)
        f.write(a+'\n')
def demo3():
    f = open('./hcp.csv', encoding='utf-8')
    a=f.read()
    print(a)


demo3()



