import functools

print(int('12345'))
print(int('12345', base=8))
print(int('12345', base=16))


def int2(i, base=2):
    return int(i, base)


print(int2('1000000'))
print(int2('1010101'))

print('=============================')

int3 = functools.partial(int, base=2)
print(int3('1000000'))
print(int3('1010101'))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
