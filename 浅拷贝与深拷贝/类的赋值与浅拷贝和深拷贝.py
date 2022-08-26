class Cpu():
    pass
class Disk():
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
# ·变量的赋值操作
# ·只是形成两个变量,实际上还是指向同一个对象
cpu1=Cpu()
disk=Disk()
cpu2=cpu1
print(cpu1)
print(cpu2)
print('--------------------------------------------------------')
# ·浅拷贝
# . Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此,源对象与拷贝对象会引用同一个子对象
computer1=Computer(cpu1,disk)
import  copy
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer1.cpu,computer1.disk)
print(computer2.__class__)

# ·深拷贝
# ·使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
print('++++++++++++++++++++++++++++++++')
computer3=copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk)
print(computer3.__class__)

