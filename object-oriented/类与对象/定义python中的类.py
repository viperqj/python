class Student:  #Student 为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace='中国'   #直接写在类里面的变量，称为类属性
    def __init__(self,name,age):
        self.name=name #self.name称为实体属性，进行了一个赋值的操作，将局部变量的name赋值给实体属性
        self.age=age

    #实例方法
    def info(self):
        print('我来自',self.native_pace,'年龄为',self.name)

    #静态方法
    @staticmethod
    def method():
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我是使用了classmethod进行修饰')

#类的组成：
    # 类属性
    # 实例方法
    # 静态方法
    # 类方法
def drink():
    print('定义在类外边的使函数')
