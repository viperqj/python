try:
    a=int(input('请输入一个数：'))
    b=int(input('请输入一个数：'))
    result=a/b
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('请输入整数')
print("程序结束")