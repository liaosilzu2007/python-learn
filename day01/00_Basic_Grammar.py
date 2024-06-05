import sys

# ================基本语法================
# 1.行与缩进
# 与C++和JAVA不一样，python使用缩进来表示代码块，不需要使用大括号 {} 。缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
'''
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误
'''

# 2.单行与多行语句
# Python语句中一般以新行作为语句的结束符，每行代码结尾不需要有标点符号，但也可以使用斜杠（\）将一行的语句分为多行显示
item_one = 'item_one'
item_two = 'item_two'
item_three = 'item_three'
total = item_one + \
        item_two + \
        item_three

# 在 [], {}, 或 () 中的多行语句，就不需要使用多行连接符
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# 3.同一行多条语句
# 每条语句用分号分隔
line_item_1 = "line_item_1";line_item2 = "line_item2";print(line_item_1 + "," + line_item2)

# 4.引号
# Python中可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 5.注释
# 单行注释使用‘#’号，多行注释使用三个单引号 ''' 或三个双引号 """。
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 6.导入
'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
'''
