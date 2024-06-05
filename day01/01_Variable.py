
# 1.变量与赋值
print("====1.变量与赋值====")
# Python中变量的赋值使用‘=’号，python中变量不需要声明类型
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

# 可以同时为多个变量赋值
a, b, c = 1, 1.317, "john"

# 变量也可以被删除，删除之后就不能再使用这个变量了
del counter, name
# print(name)




# 2.数据类型
print("====2.数据类型====")
# Python有五个标准的数据类型：Numbers（数字）、String（字符串）、List（列表）、Tuple（元组）、Dictionary（字典）

# 2.1 Numbers（数字）数据类型
print("====2.1 Numbers（数字）====")
# 数字据类型用于存储数值。他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
# 当你指定一个值时，Number 对象就会被创建：
num1 = 1
num2 = 10.5
# Python支持的数字类型有： int（有符号整型）、float（浮点型）、complex（复数）


# 2.2 String（字符串）数据类型
print("====2.2 String（字符串）====")
# 加号（+）是字符串连接运算符，星号（*）是重复操作。
# 截取字符串方式：{字符串变量}[头下标:尾下标] ，逻辑是：左闭右开，
# 其中下标是从 0 开始算起，可以是正数或负数，-1表示从倒数第一个开始取，以此类推。下标可以为空表示取到头或尾。
str = 'Hello World!'

print(str[0])       # 输出字符串中的第一个字符：H
print(str[2:5])    # 输出字符串中第三个至第六个之间的字符串：llo
print(str[2:])     # 输出从第三个字符开始的字符串：llo World!
print(str * 2)     # 输出字符串两次：Hello World!Hello World!
print(str + "TEST")  # 输出连接的字符串：Hello World!TEST


# 2.3 List（列表）数据类型
print("====2.3 List（列表）====")
# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
# 它可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表。
# 从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)           # 输出完整列表：['runoob', 786, 2.23, 'john', 70.2]
print(list[0])           # 输出列表的第一个元素：runoob
print(list[1:3])         # 输出第二个至第三个元素：[786, 2.23]
print(list[2:])         # 输出从第三个开始至列表末尾的所有元素：[2.23, 'john', 70.2]
print(tinylist * 2)     # 输出列表两次：[123, 'john', 123, 'john']
# 打印组合的列表：['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
print(list + tinylist)

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
print(letters[1:4:2])  # 输出['h', 'c']


# 2.4 Tuple（元组）数据类型
print("====2.4 Tuple（元组）====")
# Tuple（元组）有点类似于 List（列表）。用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)               # 输出完整元组：('runoob', 786, 2.23, 'john', 70.2)
print(tuple[0])          # 输出元组的第一个元素：runoob
print(tuple[1:3])       # 输出第二个至第四个（不包含）的元素：(786, 2.23)
print(tuple[2:])        # 输出从第三个开始至列表末尾的所有元素：(2.23, 'john', 70.2)
print(tinytuple * 2)      # 输出元组两次：(123, 'john', 123, 'john')
# 打印组合的元组：('runoob', 786, 2.23, 'john', 70.2, 123, 'john')
print(tuple + tinytuple)

# 因为元组不允许被二次赋值，所以如下对元组的赋值操作是会报错的，但列表不会有这个问题。
'''
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
'''

# 2.5 Dictionary（字典）
print("====2.5 Dictionary（字典）====")
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])        # 输出键为'one' 的值：This is one
print(dict[2])                # 输出键为 2 的值：This is two
# 输出完整的字典：{'dept': 'sales', 'code': 6734, 'name': 'runoob'}
print(tinydict)
print(tinydict.keys())         # 输出所有键：['dept', 'code', 'name']
print(tinydict.values())       # 输出所有值：['sales', 6734, 'runoob']


# 3.Python数据类型转换
print("====3.Python数据类型转换====")
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
'''
函数	描述
int(x [,base])      将x转换为一个整数
long(x [,base] )    将x转换为一个长整数
float(x)            将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)              将对象 x 转换为字符串
repr(x)             将对象 x 转换为表达式字符串
eval(str)           用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)            将序列 s 转换为一个元组
list(s)             将序列 s 转换为一个列表
set(s)              转换为可变集合
dict(d)             创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)        转换为不可变集合
chr(x)              将一个整数转换为一个字符
unichr(x)           将一个整数转换为Unicode字符
ord(x)              将一个字符转换为它的整数值
hex(x)              将一个整数转换为一个十六进制字符串
oct(x)              将一个整数转换为一个八进制字符串
'''
