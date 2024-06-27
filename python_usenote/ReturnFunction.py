def calc_sum(*args):
    ax = 0
    for i in args:
        ax += i
    return ax


print(calc_sum(1, 3, 5, 7, 9))


def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
# 函数返回的不是结果，而是一个函数
print(f)
print(f())
# 每次调用返回的都是一个新的函数
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f == f2)
