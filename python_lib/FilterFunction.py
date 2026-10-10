def is_odd(n):
    return n % 2 == 1


l = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(is_odd, l)))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


# def _not_divisible2(n):
#     def fn(x):
#         return x % n > 0
#     return fn(x)


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 100:
        print(n)
    else:
        break
