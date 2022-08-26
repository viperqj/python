class A():
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

def eat(self):
    pass

c=C('蔡徐坤','21')
c.eat=eat
#-------------------------------------------------------------------------------
print(c.__dict__)  #实例对象的属性字典/方法  {'name': '蔡徐坤', 'age': '21', 'eat': <function eat at 0x0000021DBE363E20>}
print(C.__dict__)
print('-------------------------------------------------------------------------------')
print(c.__class__) #<class '__main__.C'>  输出所属对象的类
print(C.__bases__) #C的父类 元组类型(<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__) #  <class '__main__.A'>挨得最近的父类
print(C.__mro__)  #类的层次结构 (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(A.__subclasses__()) #子类的列表 [<class '__main__.C'>]