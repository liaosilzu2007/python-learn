def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def factNew(n):
    return fact_iter(n, 1)


print(factNew(5))


def trim(s):
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] != " ":
            start = i
            break
    for i in range(1, len(s) + 1):
        if s[-i] != " ":
            if i == 1:
                end = len(s) + 1
            else:
                end = -i + 1
            break
    return s[start:end]


print(trim('hello  '))
print(trim('  hello'))
print(trim('  hello  '))
print(trim('  hello  world  '))
print(trim(''))
print(trim('    '))
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!')





