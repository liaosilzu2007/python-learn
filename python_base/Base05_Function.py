# ================函数================
import math
from functools import reduce

'''
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体
'''


# 1.定义并使用函数
# 示例：使用函数来输出"Hello World！"：
def hello():
    print("Hello World!")


hello()  # 输出：Hello World!


# 示例：带参数的函数，比较两个数，并返回较大的数:
def max(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(max(a, b))  # 输出：5

# 2.参数传递
'''
在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：

a=[1,2,3]

a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将列表 la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''


# 2.1 传不可变对象实例
# 示例：通过 id() 函数来查看内存地址变化：
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)
'''
以上实例输出结果为：

4379369136
4379369136
4379369424
可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。
'''


# 2.2传可变对象实例
# 示例：可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
def changelist(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changelist(mylist)
print("函数外取值: ", mylist)

'''
传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下：

函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
'''

# 3.函数参数
'''
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数
'''

# 3.1必需参数
'''
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
'''


# 示例：调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用 printme 函数，不加参数会报错
printme()
'''
以上实例输出结果：

Traceback (most recent call last):
  File "test.py", line 10, in <module>
    printme()
TypeError: printme() missing 1 required positional argument: 'str'
'''

# 3.2 关键字参数
'''
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
'''


def printinfo_1(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


#调用 printinfo_1 函数
printinfo_1(age=50, name="Jack")

'''
以上实例输出结果：

名字:  Jack
年龄:  50
'''

# 3.3 默认参数
'''
调用函数时，如果没有传递参数，则会使用默认参数。
'''


# 实列：如果没有传入 age 参数，则使用默认值：
def printinfo_2(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


#调用 printinfo_2 函数
printinfo_2(age=50, name="Jack")
print("------------------------")
printinfo_2(name="Jack")

'''
以上实例输出结果：

名字:  Jack
年龄:  50
------------------------
名字:  Jack
年龄:  35
'''

# 3.4 不定长参数
'''
一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述几种参数不同，声明时不会命名。

可以传两种类型的参数。带一个星号 “*” 的参数会以元组(tuple)的形式传入，存放所有未命名的变量参数。
def 函数名([formal_args,] *var_args_tuple ):
    函数体

带两个星号 “**” 的参数会以字典的形式传入。
def 函数名([formal_args,] **var_args_dict ):
    函数体
'''


# 示例：传入元组类型的可变参数
def printinfo_3(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用 printinfo_3 函数
printinfo_3(70, 60, 50)

'''
以上实例输出结果：

输出: 
70
(60, 50)
'''


# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
def printinfo_4(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用 printinfo_4 函数
printinfo_4(10)
printinfo_4(70, 60, 50)

'''
以上实例输出结果：

输出:
10
输出:
70
60
50
'''


# 声明函数时，参数中星号 * 可以单独出现，例如:
def fun_01(a, b, *, c):
    return a + b + c


# 注意：如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
fun_01(1, 2, 3)  # 报错
'''
报错如下：
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
'''
fun_01(1, 2, c=3)  # 正常


# 示例：传入字典类型的可变参数
def printinfo_5(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用 printinfo_5 函数
printinfo_5(1, a=2, b=3)

'''
以上实例输出结果：

输出: 
1
{'a': 2, 'b': 3}
'''

# 4.强制位置参数
'''
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
'''


# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def func_2(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


#以下使用方法是正确的:
func_2(10, 20, 30, d=40, e=50, f=60)

#以下使用方法会发生错误:
func_2(10, b=20, c=30, d=40, e=50, f=60)  # b 不能使用关键字参数的形式
func_2(10, 20, 30, 40, 50, f=60)  # e 必须使用关键字参数的形式

# 5.匿名函数（lambda函数）
'''
Python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，例如在 map()、filter()、reduce() 等函数中。

(1) lambda 只是一个表达式，函数体比 def 简单很多。
(2) lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
(3) lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
(4) 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。
语法
lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression
'''
# 示例
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))  #输出：30
print("相加后的值为 : ", sum(20, 20))  #输出：40


#可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
#示例：以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  #输出：22
print(mytripler(11))  #输出：33

# 示例：使用 lambda 函数与 map() 函数联合使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

# 示例：使用 lambda 函数与 filter() 函数联合使用
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8] 

# 示例：使用 reduce() 和 lambda 函数计算累计乘积
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # 输出：120   # reduce() 函数通过遍历 numbers 列表，并使用 lambda 函数将累积的结果不断更新，最终得到了 1 * 2 * 3 * 4 * 5 = 120 的结果。
