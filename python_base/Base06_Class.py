# ================面向对象================
"""
Python从设计之初就已经是一门面向对象的语言，所以支持像Java一样的面向对象编程。
面向对象简介：
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：也即Java中的静态变量。类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
局部变量：定义在方法中的变量，只作用于当前实例的类。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
实例化：创建一个类的实例，类的具体对象。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
"""

# 1.类
'''
定义类的语法格式如下：
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
'''


# 2.对象
# 类实例化后生成对象，然后这个对象可以作为属性引用。Python 中所有的属性引用使用一样的标准语法：obj.name。
class HelloClass:
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = HelloClass()

# 访问类的属性和方法
print("HelloClass 类的属性 i 为：", x.i)            # 输出：HelloClass 类的属性 i 为： 12345
print("HelloClass 类的方法 f 输出为：", x.f())      # 输出：HelloClass 类的方法 f 输出为： hello world

# 3.方法
'''
类的方法与普通的函数只有一个特别的区别：类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。self 的名字并不是规定死的，也可以使用 this，但是最好还是按照使用惯例采用 self 作为参数名。
'''


class TestSelf:
    def prt(self):
        print(self)
        print(self.__class__)


testSelf = TestSelf()                       # 输出：<__main__.TestSelf object at 0x0000015B9B70BDF0>
testSelf.prt()                              # 输出：<class '__main__.TestSelf'>
# 从上面执行结果可以看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

# 3.1 构造方法
'''
类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用。类似Java中的默认构造器方法。
当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
'''


class InitTest:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


initTest = InitTest(3.0, -4.5)
print(initTest.r, initTest.i)           # 输出：3.0 -4.5


# 普通方法中可以访问构造方法中给实例添加的属性。
class InitTest2:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)


initTest2 = InitTest2(42)
initTest2.display_value()               # 输出：42

# 4.私有属性和私有方法
'''
类似于Java中 private 修饰的属性和方法
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
'''


# 示例：私有属性
class PrivateCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)


counter = PrivateCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量


# 示例：私有方法
class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()


site = Site('百度', 'www.baidu.com')
site.who()        # 正常输出
site.foo()        # 正常输出
site.__foo()      # 报错

# 5.继承
'''
继承是面向对象的一个特征。
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
父类必须与子类定义在一个作用域内。
继承的语法格式如下：
class DerivedClassName(modname.BaseClassName):
'''


# 示例：单继承
class People:

    name = ''
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))


class Student(People):
    grade = ''

    def __init__(self,n,a,w,g):
        # 调用父类的构函
        People.__init__(self,n,a,w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))


student = Student('ken',10,60,3)
student.speak()                         # 输出：ken 说: 我 10 岁了，我在读 3 年级

# 5.1 多继承
'''
Python支持多继承形式。
多继承的类定义形如下：
class DerivedClassName(Base1, Base2, Base3):

需要注意圆括号中父类的顺序，若是父类中有相同的方法名，子类又未重写该方法，且在子类使用时未指定父类，则会从左到右查找父类中是否包含该方法。
'''


# 示例：多继承
class Speaker():
    topic = ''
    name = ''

    def __init__(self,n,t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))


class Sample(Speaker,Student):
    a =''

    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)


sample = Sample("Tim",25,80,4,"Python")
sample.speak()              # 输出：我叫 Tim，我是一个演说家，我演讲的主题是 Python             #方法名同，默认调用的是在括号中参数位置排前父类的方法

# 6.方法重写
'''
子类可以重写父类的方法。
重写之后如果子类还想调用父类方法，可以使用super()函数。
'''


class Parent:        # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent): # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()          # 子类实例
c.myMethod()           # 子类调用重写方法              #输出：调用子类方法
super(Child,c).myMethod()      # 用子类对象调用父类已被覆盖的方法             # 输出：调用父类方法
