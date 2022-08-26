# object类
    # object类是所有类的父类，因此所有类都有object类的属性和方法。
    # 内置函数dir()可以查看指定对象所有属性
    # Object有一个_str_()方法，用于返回一个对于“对象的描述",对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对_str_()进行重写
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是%s,年龄%s'%(self.name,self.age)


stu=Student('kk',20)
print(dir(stu))
print(stu)