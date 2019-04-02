# class Student():
#     name = "admin"
#     age = 18
# Student.__dict__
#
# #实例化
# yueyue = Student()
# yueyue.__dict__
# print(yueyue.name)
#
# class A():
#     name = "dana"
#     age = 18
#     def say(self):
#         self.name = "aaa"
#         self.name = "200"
#
# #此案例说明：类实例的属性和其对象的实例的属性在不对对象的实力属性赋值的前提下
# #指向同一个变量
#
# #A称为类的实例
# print(A.name)
# print(A.age)
#
# print("*" * 20)
#
# #id可以鉴别一个变量和另一个变量是否一样
# print(id(A.name))
# print(id(A.age))
#
# a = A()
#
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))
#
# print("********************************")
#
# #关于self的案例
# class A():
#     name = "zl"
#     age = 15
#     def __init__(self):
#         self.name = "aaaa"
#         self.age = 200
#
#     def say(self):
#         print(self.name)
#         print(self.age)
#
# class B():
#     name = "bbbbb"
#     age = 90
#
# a = A()
# a.say()
#
# print("********************************")
# A.say(A)
# A.say(B)
#
# print("********************************")
# class Person():
#     # name是共有的成员
#     name = "liuying"
#     # __age就是私有成员
#     __age = 18
# P = Person()
# print(P.name)
# print(P._Person__age)
# print(P.__dict__)
# print("********************************")

class Person():
    name = "NoNO"
    age = 0
    __score = 0 #成绩  私有，
    _petname = "sec"  #小名受保护子类可用，不能公用
    def sleep(self):
        print("sleep......")
    def work(self):
        print("make money")

class Teacher(Person):
    teacher_id = "46"
    name = "MM  "
    def make_test(self):
        print("attention")

    def work(self):
        Person.work(self)
        self.make_test()
        super().work()      #super代表得到父类

n = Person()
t = Teacher()
t.work()

class Anminel():
    def __init__(self):
        print("I am a PX")

class PaxingAn(Anminel):
    def __init__(self,name):
        print("I am a PX {0}".format(name))

class Dog(PaxingAn):
    def __init__(self):
        print("I am a PX")

class Cat(PaxingAn):
    pass

d = Dog()
c = Cat("Two")




