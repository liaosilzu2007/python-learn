# ================迭代器和生成器================

# 1.迭代器
"""
(1)什么是迭代？
迭代是一个遍历数据集合元素的过程。从第一个元素开始访问，一次只访问一个元素，直到最后一个元素访问完后迭代结束。
在Python中，迭代通常用于遍历序列（如列表、元组）或任何可迭代对象。并且在python中迭代只能往前，不能往后。
"""
# 示例：一个遍历列表的典型方式
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print("简单for循环遍历：" + fruit)

'''
(2)迭代器
迭代器是python中实现迭代功能的工具。有两个基本的方法：iter() 和 next()。iter()方法用于返回一个迭代器对象，而next()方法则返回迭代器的下一个值。当没有更多的值可返回时，next()方法会抛出StopIteration异常。
'''
list_test = [1, 2, 3, 4]
it_01 = iter(list_test)  # 创建迭代器对象

print(next(it_01))  # 1
print(next(it_01))  # 2
print(next(it_01))  # 3

# 2.内置迭代器
'''
Python的许多内置类型和函数返回迭代器，例如range()、enumerate()、filter()、map()等。
'''
# 示例：使用range()返回迭代器
for i in range(5):
    print("range()迭代器遍历：" + str(i))  # 输出: 0, 1, 2, 3, 4

# 示例：使用enumerate()返回迭代器
# enumerate()函数将可迭代对象转换为一个枚举对象，同时提供索引和值。这在处理需要跟踪索引的情况中非常有用。
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print("enumerate()迭代器遍历：" + f"Index: {index}, Fruit: {fruit}")

# 示例：使用filter()返回迭代器
# filter()可以对可迭代对象的元素进行过滤。例如，过滤出偶数：
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
for num in even_numbers:
    print("filter()迭代器遍历：" + str(num))

# 示例：使用map()返回迭代器
# map()函数可以对可迭代对象的元素进行映射操作。例如，映射平方操作：
squared = map(lambda x: x ** 2, numbers)
for square in squared:
    print("map()迭代器遍历：" + str(square))

# 3.自定义迭代器
'''
自定义迭代器允许我们创建自己的数据结构并以迭代方式访问其内容。在Python中，最常见的方式是通过生成器函数来实现。另外也可以直接定义类来实现__iter__和__next__方法，实现了这两个方法之后，对象可以进行迭代访问。
'''


# 示例：直接定义类实现__iter__和__next__方法
class NumberSequenceIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result


# 使用自定义迭代器
seq_iter = NumberSequenceIterator(1, 5)
print(next(seq_iter))
print(next(seq_iter))
for num in seq_iter:
    print("直接定义类实现__iter__和__next__方法：" + str(num))

# 3.1 生成器
'''
在python中，yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，该函数的返回值是一个生成器（generator），而不是一次性返回一个包含所有结果的数据集合。我们可以通过next()方法或者for循环（也即是迭代的方法）从生成器中依次取出数据集合。

yield关键字有语句暂停和恢复函数执行的作用，迭代时，会在yield语句暂停，并返回有yield修饰的变量或表达式的值，在下次迭代时，会从上次暂停的位置继续执行（即执行yeild语句的下一行代码），直到再次遇到 yield 语句。
简要理解：执行 yield 语句就是 return 一个值，并且记住这个位置，下次迭代就从这个位置后(下一行)开始。
'''


def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
generator = countdown(5)

# 通过next()获取集合中的下一个值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print("通过生成器遍历：" + str(value))  # 输出: 2 1

# 3.2 生成器表达式
'''
除了生成器函数，Python还提供了生成器表达式，它是一种简洁的创建生成器的方式，类似于列表推导式，但不会立即计算所有结果：
'''
squares = (x ** 2 for x in range(10))
for square in squares:
    print("生成器表达式创建的生成器遍历：" + str(square))

# 4.迭代器的优缺点
'''
(1)优点
迭代器最大的优点之一是其惰性计算特性。这意味着它不会一次性生成所有数据，而是在需要时按需生成，所以内存开销较小。这对于处理大数据集或无限序列特别有用，因为它们只占用有限的内存。
(2)缺点
迭代器不支持反向迭代，这在某些情况下可能会成为限制。
迭代器通常在第一次迭代后不再可用，因此需要谨慎处理。如果需要多次迭代，应确保每次迭代都有新的迭代器。
在多线程环境中，迭代器需要额外的同步措施，以防止数据竞争。
'''
