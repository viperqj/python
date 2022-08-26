# try..except..else 结构
#     如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
try:
    a=int(input('请输入一个数：'))
    b=int(input('请输入一个数：'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print("结果为",result)