# ·以主程序形式运行
    # ·在每个模块的定义中都包括一个记录模块名称的变量_name__,程序可以检查该变量，以确定他们在哪个模块中执行。
    # 如果一个模块不是被导入到其它程序中执行，那么它可能在解释器的顶级模块中执行。顶级模块的_name__变量的值为_main_
def add(a,b):
    print(a+b)


if __name__ == '__main__':
    add(10,20)

