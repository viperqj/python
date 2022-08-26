#  Python是动态语言，在创建对象之后，可以动态地绑定属性和方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('qj',21)
stu2=Student('cxk',22)
print(id(stu1))
print(id(stu2))

print('-----------为stu1动态绑定属性--------------')
stu1.gender='女'
print(stu1.gender)

print('----------------动态绑定方法---------------')
def show():
    print('定义在类之外的是函数')
stu1.show=show
stu1.show()
Student.show=show
Student.show()