# ================异常================
"""
异常：指语法正确，在运行时检测出的错误。
Python 异常处理的关键字：try、except、else、raise、finally
"""

import sys

# 1.异常
'''
大多数的异常都不会被程序处理，会以错误信息的形式打印出来，包括异常的类型，具体的模块，以及调用栈等。
例如：
>>> 10 * (1/0)             # 0 不能作为除数，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: division by zero
>>> 4 + spam*3             # spam 未定义，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined
>>> '2' + 2               # int 不能与 str 相加，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

'''

# 2.异常处理

# 2.1 try/except
# 示例：让用户输入一个整数，如果是非整数，则会报错
# try:
#     x = int(input("请输入一个数字: "))
# except ValueError:
#     print("您输入的不是数字！")

# print("您输入的数字为："+ str(x))

'''
try 语句按照如下方式工作；
(1) 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
(2) 如果没有异常发生，忽略 except 子句，try 子句执行后结束。
(3) 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
(4) 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
例如：
except RuntimeError:
    执行语句1
except TypeError:
    执行语句2
except NameError:
    执行语句3

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
except (RuntimeError, TypeError, NameError):
    pass
    
另外，对于异常类型还可以使用别名，在此except子句中就可以使用该别名。
例如：
except OSError as err:
    print("OS error: {0}".format(err))

'''
# 示例：最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# 2.2 异常的else
'''
try/except 语句还有一个可选的 else 子句：try/except...else。else子句必须放在所有的 except 子句之后。else 子句将在 try 子句没有发生任何异常的时候执行。

使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。
'''

try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else子句中的代码')


# 2.3 异常的finally
'''
 finally表示的是⽆论是否异常都要执⾏的代码，例如关闭⽂件。
'''
# finally示例
try:
   f = open('test.txt', 'r')
except Exception as result:
   f = open('test.txt', 'w')
else:
   print('读取文件没有异常')
finally:
   f.close()


# 2.4 异常的抛出（raise）
'''
Python 使用 raise 语句抛出一个指定的异常。

raise语法格式如下：

raise [Exception [, args [, traceback]]]

可以抛出Python语言基础包中的异常（比如前面2.1节中，如果没有匹配到异常类型，使用raise抛出异常），也可以抛出自定的异常。
'''


# 2.5 自定义异常
'''
可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
'''
# 示例：抛出自定的异常。
# 示例需求：密码⻓度不⾜，则报异常（⽤户输⼊密码，如果输⼊的⻓度不⾜ 3 位，则报错，即抛出⾃定义异常，并捕获该异常）。

class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len
 
    # 设置抛出异常的描述信息
    def __str__(self):
        return f'您输⼊的⻓度是{self.length}, 不能少于{self.min_len}个字符'             # f+字符串，python 3.6新加的一种字符串格式化，与 str.format() 功能相同
 
 
def inputpwd():
    try:
        con = input('请输⼊密码：')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)          # 抛出自定义异常
    except Exception as e:
        print(e)
    else:
        print('密码已经输⼊完成')
 
inputpwd()


# 2.6 预定义的清理行为
'''
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
比如读取一个文件的内容，代码执行完毕后，文件会保持打开状态，并没有被关闭。通常我们会在finally子句中进行关闭动作。但也可以通过其他语句来实现读取完后的关闭动作。
在java1.7以后版本中，就可以使用  try (InputStream is = new FileInputStream(file)) { ...... } catch (Exception e) { ...... } 来实现
在python中，关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

'''
# 示例：使用with语句。就算在处理过程中出问题了，文件 f 总是会关闭。
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# 2.7 带异常处理语句方法的返回值问题
# 2.7.1 在函数中使用try语句，如果finally中出现return，无论是否有异常，都返回finally中的返回值
def func_try_except():
    try:
        print("程序正常运行。。。")
        return 1
    except KeyError:
        print('key error错误。。。')
        return 2
    else:
        print("程序未产生异常时则运行当前代码。。。")
        return 3
    finally:
        print("程序无论是否出现异常都执行此语句。。。")
        return 4
 
res = func_try_except()
print(res)

# 输出
'''
程序正常运行。。。
程序无论是否出现异常都执行此语句。。。
4
'''

 
# 2.7.2 在函数中使用try语句，如果finally子句中没有return语句，并且没有异常，则返回try中的返回值
def func_try_except2():
    try:
        print("程序正常运行。。。")
        return 1
    except KeyError:
        print('key error错误。。。')
        return 2
    else:
        print("程序未产生异常时则运行当前代码。。。")
        return 3
    finally:
        print("程序无论是否出现异常都执行此语句。。。")
        # return 4
 
res2 = func_try_except2()
print(res2)

# 输出
'''
程序正常运行。。。
程序无论是否出现异常都执行此语句。。。
1
'''

 
# 2.7.3 在函数中使用try语句，如果finally子句中没有return语句，并且有异常抛出，则返回异常子句中的返回值
def func_try_except3():
    try:
        print("程序正常运行。。。")
        raise KeyError
        return 1
    except KeyError:
        print('key error错误。。。')
        return 2
    else:
        print("程序未产生异常时则运行当前代码。。。")
        return 3
    finally:
        print("程序无论是否出现异常都执行此语句。。。")
        
res3 = func_try_except3()
print(res3)

# 输出
'''
程序正常运行。。。
key error错误。。。
程序无论是否出现异常都执行此语句。。。
2
'''
