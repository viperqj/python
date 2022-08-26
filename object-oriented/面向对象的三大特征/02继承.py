class Person(object): #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,sno):
        super().__init__(name,age)
        self.sno=sno

class Teacher(Person):
    def __init__(self,name,age,tno):
        super().__init__(name,age)
        self.tno=tno

stu=Student('kk',15,'100')
teacher=Teacher('aa',20,5)

stu.info()
teacher.info()

#多继承
class A(Teacher,Student):
    pass
