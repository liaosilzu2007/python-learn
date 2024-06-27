print(abs(-10))
print(abs)
f = abs
print(f)
print(f(-20))


# 一个函数可以接收另一个函数作为参数，这样的函数称为高阶函数
def add(x, y, func):
    return func(x) + func(y)


print(add(-5, 6, f))
