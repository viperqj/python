# ·类属性:类中方法外的变量称为类属性，被该类的所有对象所共享
# ·类方法:使用@classmethod修饰的方法，使用类名直接访问的方法
# ·静态方法:使用@staticmethod修饰的主法，使用类名直接访问的方法

from 定义python中的类 import Student


#类属性的使用方式
# print(Student.native_pace)
stu1=Student('qj',21)
stu2=Student('cxk',8)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='山西'
print(stu1.native_pace)
print(stu2.native_pace)
    #动态添加类属性
Student.detail='练习两年半'
print(Student.detail)

print('----------类方法的使用方式------------')
stu1.cm()

print('----------静态方法的使用方式------------')
Student.method()