# ================装饰器================
"""
迭代器、生成器和装饰器是python中的3个重要功能，其中装饰器属于较难的一个内容。

什么是装饰器？装饰器可以做什么？
要理解python中的装饰器，可以参考设计模式中的装饰器模式，装饰器模式的作用是在开闭原则的基础上，对已有功能进行功能扩展。比如系统已有一个功能是生成各种图形（比如圆形、长方形、扇形），现在有个需求是要对生成的图形增加红色的边界，那就可以使用装饰器模式来改造。再比如现在有一些业务处理过程，现在想记录这些过程处理的时间，在Java项目中，可以通过切面等方法来实现，在python中，则可以通过装饰器来实现。

总结：在Python中，装饰器本质上是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是允许在不修改原有代码的基础上，为已经存在的函数或对象添加额外的功能。

"""

# 1.装饰器的写法
'''
在python中装饰器怎么编写呢？
首先，装饰器分为函数装饰器和类装饰器。函数装饰器是一个函数，它接受一个函数（例如func）作为参数，并返回一个内部函数（例如wrapper），在这个内部函数（指wrapper）内部，你可以执行一些额外的操作，然后调用原始函数（指func），并返回其结果。
'''


# 1.1 装饰器的早期写法
# 在早期 (Python版本 < 2.4，2004年以前)，函数装饰器的写法如下。
# 示例：为一个已有的方法，增加日志打印功能
def debug_log(func):
    def wrapper():
        print("[DEBUG]: enter {}".format(func.__name__))
        return func()

    return wrapper


def say_hello():
    print("hello python!")


say_hello1 = debug_log(say_hello)  # 添加功能并保持原函数名不变
say_hello1()  # 调用装饰后的方法


# 1.2 装饰器的语法糖写法
# 因为早期写法不够优雅，所以后期版本中，支持语法糖写法，有点像java中的注解。
@debug_log
def say_hello2():
    print("hello java!")


say_hello2()

# 2. 带参数的装饰器
# 2.1 如果被装饰的函数需要传入参数，那装饰器函数要怎么写呢？一个简单的做法指定装饰器函数wrapper接受和原函数一样的参数。比如：
print("*******************2. 带参数的装饰器*******************示例1")


def debug_log2(func):
    def wrapper(something):  # 指定一样的参数
        print("[DEBUG]: enter {}".format(func.__name__))
        return func(something)

    return wrapper  # 装饰器函数返回包装过的函数


@debug_log2
def say(something):
    print("hello {}!".format(something))


say("hadoop")

# 2.2 但是函数有千千万万，不同的函数的参数不尽相同，想要有通用的传参方法，需要用到python里的可变参数*args和关键字参数**kwargs，有了这两个参数，装饰器就可以用于任意目标函数了。
print("*******************2. 带参数的装饰器*******************示例2")


def debug_log3(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...', )
        return func(*args, **kwargs)

    return wrapper


@debug_log3
def say2(something):
    print("hello {}!".format(something))


say2("oracle")

# 2.3 如果上面的日志装饰器不仅需要在进入某个函数后打出日志信息，而且还需要能够指定log的级别，那么装饰器则需要这样写。
print("*******************2. 带参数的装饰器*******************示例3")


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}".format(level=level, func=func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@logging(level='INFO')  # 将日志级别通过参数名方法传入装饰器函数
def say3(something):
    print("say3 {}!".format(something))


# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print("do {}...".format(something))


say3('hello')
do("my work")

# 3. 类装饰器
'''
除了函数装饰器，还有类装饰器。如果让类的构造函数__init__()接受一个函数，然后重载__call__()方法并返回一个函数，就实现了类装饰器。
'''
print("*******************3. 类装饰器*******************示例1")


class LogClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}".format(func=self.func.__name__))
        return self.func(*args, **kwargs)


@LogClass
def say4(something):
    print("say4 {}!".format(something))


say4("javascript")

# 如果需要在类装饰器实现参数的传入，则需要在__init__()方法中将参数传入。而函数的传入不再从__init__()方法传入，要在重载__call__方法传入函数，并且返回包装过的函数。
# 示例：比如传入上文中的日志级别：
print("*******************3. 类装饰器*******************示例2")


class LogClass2:
    def __init__(self, level='DEBUG'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)

        return wrapper


@LogClass2(level='INFO')
def say5(something):
    print("say5 {}!".format(something))


say5("C#")

# 4.多个装饰器的顺序
'''
一个函数可以被多个装饰器进行装饰，那么装饰器的执行顺序是怎么样的呢？执行一下下面的代码就清楚了
'''
print("*******************4.多个装饰器的顺序*******************示例1")


def decorator_1(func):
    def wrapper(*args, **kwargs):
        print('我是装饰器1')
        func(*args, **kwargs)

    return wrapper


def decorator_2(func):
    def wrapper(*args, **kwargs):
        print('我是装饰器2')
        func(*args, **kwargs)

    return wrapper


def decorator_3(func):
    def wrapper(*args, **kwargs):
        print('我是装饰器3')
        func(*args, **kwargs)

    return wrapper


@decorator_1
@decorator_2
@decorator_3
def hello3():
    print("multi decorator test")


hello3()

'''
输出结果：
我是装饰器1
我是装饰器2
我是装饰器3
multi decorator test

原因：上面多装饰器语法糖可以看作如下代码，hello3 = decorator_1(decorator_2(decorator_3(hello3)))，由里到外依次执行装饰器的内容。
'''

# 4.内置的装饰器
'''
内置的装饰器和普通的装饰器原理是一样的，只不过返回的不是函数，而是类对象，所以更难理解一些。
'''
