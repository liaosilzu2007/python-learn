from functools import reduce


# map()函数是将传入的函数依次作用到序列的每个元素
def f(x):
    return x * x


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, l1)
print(list(r))
print(list(map(str, l1)))

l2 = [1, 3, 5, 7, 9]


def add(x, y):
    return x + y


'''
reduce()函数是把函数作用在一个序列上，这个函数必须接收两个参数,
reduce把函数的结果继续和序列的下一个元素作累积计算
'''
print(reduce(add, l2))

print("============================")
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(a):
    return DIGITS[a]


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(char2num, s))


print(str2int("1357"))


# 使用lambda表达式
def str2int_lambda(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int_lambda("13579"))
