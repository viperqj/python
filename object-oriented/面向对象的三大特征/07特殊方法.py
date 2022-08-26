a=20
b=21
c=a+b
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):#实现了两个对象相加
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('蔡徐坤')
stu2=Student('林俊杰')
print(stu1+stu2)
print(stu1.__add__(stu2))
print(stu1.__len__())