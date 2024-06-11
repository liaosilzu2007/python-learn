# ================语句================

# 1.条件控制语句
# 1.1 if语句
"""
if语句的格式：

if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

注意：

1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case，功能也类似，详见下文。

"""
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

'''
执行以上代码，输出结果为：

1 - if 表达式条件为 true
100
Good bye!

从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行。
'''

# 1.2 if嵌套语句
'''
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''

# 1.3 match...case
'''
Python 3.10 增加了 match...case 的条件判断，不需要再使用一连串的 if-else 来判断了。

match 后的对象会依次与 case 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，_ 可以匹配一切。

语法格式如下：

match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
case _: 类似于 C 和 Java 中的 default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功。


一个 case 也可以设置多个匹配条件，条件使用 ｜ 隔开，例如：
case 401|403|404:
    return "Not allowed"
'''

# 2.循环语句
# 2.1 while 循环
'''
Python 中 while 语句的一般形式：

while 判断条件(condition)：
    执行语句(statements)……

同样需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环。

以下实例使用了 while 来计算 1 到 100 的总和：
'''

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))  # 输出：1 到 100 之和为: 5050

# 2.1.1无限循环
# 我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：
var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)

print("Good bye!")

'''
执行以上脚本，输出结果如下：

输入一个数字  :5
你输入的数字是:  5
输入一个数字  :

你可以使用 CTRL+C 来退出当前的无限循环。
无限循环在服务器上客户端的实时请求非常有用。
'''

# 2.1.2 while 循环使用 else 语句
'''
如果 while 后面的条件语句为 false 时，则执行 else 的语句块。

语法格式如下：

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>

运行逻辑：expr 条件语句为 true 则执行 statement(s) 语句块，如果为 false，则执行 additional_statement(s)。

循环输出数字，并判断大小：
'''
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

'''
执行以上脚本，输出结果如下：

0  小于 5
1  小于 5
2  小于 5
3  小于 5
4  小于 5
5  大于或等于 5
'''

# 2.1.3 简单语句组
# 类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与 while 写在同一行中， 如下所示：

flag = 1

while (flag): print('欢迎访问Github!')

print("Good bye!")

'''
注意：以上的无限循环你可以使用 CTRL+C 来中断循环。

执行以上脚本，输出结果如下：

欢迎访问Github!
欢迎访问Github!
欢迎访问Github!
欢迎访问Github!
欢迎访问Github!
……
'''

# 2.for循环
# 2.1 简单for语句
'''
Python 的 for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

'''
以上代码执行输出结果为：

Baidu
Google
Runoob
Taobao
'''

# 也可用于打印字符串中的每个字符：

word = 'runoob'

for letter in word:
    print(letter)

'''
以上代码执行输出结果为：

r
u
n
o
o
b
'''

# 整数范围值可以配合 range() 函数使用： 
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)

'''
以上代码执行输出结果为：

1
2
3
4
5
'''

# 2.2 for...else
'''
在 Python 中，for...else 语句用于在循环结束后执行一段代码。

语法格式如下：

for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码
当循环执行完毕（即遍历完 iterable 中的所有元素）后，会执行 else 子句中的代码，如果在循环过程中遇到了 break 语句，则会中断循环，此时不会执行 else 子句。
'''
for x in range(6):
    print(x)
else:
    print("Finally finished!")

'''
执行脚本后，输出结果为：

0
1
2
3
4
5
Finally finished!
'''

# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体，不会执行 else 子句：
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

'''
执行脚本后，在循环到 "Runoob"时会跳出循环体：

循环数据 Baidu
循环数据 Google
菜鸟教程!
完成循环!
'''

# 2.3 break 和 continue
'''
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句是用来跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''
# 示例：break的使用
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当前变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

'''
执行以上脚本输出结果为：

当前字母为 : R
当前字母为 : u
当前字母为 : n
当前字母为 : o
当前字母为 : o
当前变量值为 : 10
当前变量值为 : 9
当前变量值为 : 8
当前变量值为 : 7
当前变量值为 : 6
Good bye!
'''

# 示例：continue的使用
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

'''
执行以上脚本输出结果为：

当前字母 : R
当前字母 : u
当前字母 : n
当前字母 : b
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
当前变量值 : 4
当前变量值 : 3
当前变量值 : 2
当前变量值 : 1
当前变量值 : 0
Good bye!
'''

# 2.4 range() 函数
# 如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，例如:
for i in range(5):
    print(i)
'''
输出：
0
1
2
3
4
'''

# 你也可以使用 range() 指定区间的值：
for i in range(5, 9):
    print(i)
'''
输出：
5
6
7
8
'''

# 也可以使 range() 以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
    print(i)
'''
输出：
0
3
6
9
'''

for i in range(-10, -100, -30):
    print(i)
'''
输出：
-10
-40
-70
'''

# 还可以结合 range() 和 len() 函数以遍历一个序列的索引,如下所示:
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
'''
输出
0 Google
1 Baidu
2 Runoob
3 Taobao
4 QQ
'''

# 还可以使用 range() 函数来创建一个列表：
b = list(range(5))  # 输出：[0, 1, 2, 3, 4]

# 2.5 pass语句
'''
Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，如下实例
'''
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

'''
执行以上脚本输出结果为：

当前字母 : R
当前字母 : u
当前字母 : n
执行 pass 块
当前字母 : o
执行 pass 块
当前字母 : o
当前字母 : b
Good bye!
'''
