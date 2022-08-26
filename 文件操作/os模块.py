# ·os模块是Python内置的与操作系统功能和文件系统相关的模块,该模块中的语句的执行结果通常与操作系统有关，
        # 在不同的操作系统上运行，得到的结果可能不一样。
# ·os模块与os.path模块用于对目录或文件进行操作
import os
# os.system('notepad.exe')
# os.system('calc.exe')
# 直接调用可执行文件
# os.startfile(r'D:\Google\Chrome\Application\chrome.exe')

# 相关函数
print(os.getcwd())#返回当前的工作目录
print(os.listdir('../文件操作'))#返回指定路径下的文件和目录信息
os.mkdir('测试')#创建目录
os.rmdir('测试')#删除目录
os.makedirs('a/b/c')#创建多级目录
os.removedirs('a/b/c')#删除多级目录


















