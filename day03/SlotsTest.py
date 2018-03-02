from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 绑定后调用实例方法
print(s.age)

'''
给实例绑定的方法，对另一个实例是不起作用的，
为了给所有实例都绑定方法，可以给class绑定方法
'''
s2 = Student()
# s2.set_age(20)


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)


'''
__slots__ 可以用来限制实例的属性
__slots__定义只对当前类的实例起作用，对子类的实例不起作用
'''


class Teacher(object):
    __slots__ = ('name', 'age')


t = Teacher()
t.name = "Paul"
t.age = 40
t.email = 'paul@gmail.com'
