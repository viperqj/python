# ·面向对象的三大特征
#   ·封装:提高程序的安全姓
#        ·将数据（属性）和行为(方法)包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
#        ·在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”。
#    ·继承:提高代码的复用性
#    ·多态:提高程序的可扩展性和可维护性

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动。。。')
car=Car('梅赛德斯')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.__age=age
        self.__gender=gender
    def show(self):
        print(self.name+'练习俩年半'+'性别'+self.__gender,'年龄',self.__age)

stu=Student('cxk',21,'女')
stu.show()
# 在类的外面使用name,age,gender
print(stu.name)
#print(stu.__age)     AttributeError: 'Student' object has no attribute '__age'
# print(dir(stu))
print(stu._Student__gender) #在类的外部可以使用 _Student__age访问