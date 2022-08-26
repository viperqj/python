class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__()方法被调用执行了，cls的id为%s'%(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id%s'%(id(obj)))
        return obj
    def __init__(self,name,age):
        print('init方法被调用，self的id为%s'%(id(self)))
        self.name=name
        self.age=age

print('object这个类的对象的id为',id(object))
print('person这个类的对象的id为',id(Person))

stu=Person('蔡徐坤',20)
print('person类的实例对象的id为%s'%(id(stu)))