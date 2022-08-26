# try..except..else..finally结构：
#     finally块无论是否发生异常都会被执行，能用来释放try中申请的资源
#     try-except-finally
#     try-else-finally
try:
    a=int(input('请输入一个数：'))
    b=int(input('请输入一个数：'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print("结果为",result)
finally:
    print('无论是否异常总会被执行的代码')
print('程序结束')