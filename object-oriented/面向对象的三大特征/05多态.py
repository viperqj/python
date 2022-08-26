class Animal():
    def eat(self):
        print('动物会吃。。。')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Person(object):
    def eat(self):
        print('人要好好学习')


def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
