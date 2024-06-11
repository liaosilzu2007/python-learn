# ================模塊================
"""
我们可以使用 python 解释器来编程，但如果从 Python 解释器退出再进入，那么定义的所有的方法和变量就都消失了。

为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。

模块是一个包含所有定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

"""
import os.path
# 下面是一个使用 python 标准库中模块的例子
import sys

'''
os.path.abspath(file)获取到的是当前文件的绝对路径；
os.path.dirname(os.path.abspath(file))获取到的是当前文件所在目录的路径
os.path.dirname(os.path.dirname(os.path.abspath(file)))获取到的是当前文件所在目录的上一级目录（本项目是 python-learn 目录）的路径。
使用sys.append()命令把路径添加到环境变量后，才可以导入python-learn 目录下的各个模块
'''
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import python_base.Base05_Function

#
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

'''
1) import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
2) sys.argv 是一个包含命令行参数的列表。
3) sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
'''

# 1.import 语句
'''
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]
import 语句需要放在脚本的顶端。一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。

当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？
这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。
这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在 sys 模块中的 path 变量，也就是上面代码打印的 sys.path 的列表。

引入之后，我们就可以通过模块名称来访问函数、变量。并且这些函数和变量可以赋一个本地名称。
比如：listFrom05 = Day05_Function.mylist
'''

# 2.from … import 语句
'''
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
from modname import name1[, name2[, ... nameN]]

例如，要导入模块 fibo 的两个函数，使用如下语句：
from fibo import fib1, fib2

这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。
'''

# 3.from … import * 语句
'''
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *

这提供了一个简单的方法来导入一个模块中的所有项目。但是那些由单一下划线（_）开头的名字不会导入。
大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。
'''

# 4.包
'''
包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。

目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，最简单的情况，放一个空的 :file:__init__.py就可以了。

如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
以下实例在 file:sounds/effects/__init__.py 中包含如下代码:
__all__ = ["echo", "surround", "reverse"]
这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。

通常我们并不主张使用 * 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。
记住，使用 from Package import specific_submodule 这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。
'''

