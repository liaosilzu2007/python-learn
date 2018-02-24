L = [x * x for x in range(5)]
print(L)

g = (x * x for x in range(5))
print(g)

for i in g:
    print(i)


print('====================')


def fib(max):
    m, a, b = 0, 0, 1
    while m < max:
        print(b)
        a, b = b, a + b
        m = m + 1
    return 'done'


print(fib(6))


def fibGenerator(max):
    j, a, b = 0, 0, 1
    while j < max:
        yield b
        a, b = b, a + b
        j += 1
    return 'done'


print('------------------')
print(fibGenerator(6))
for n in fibGenerator(6):
    print(n)

g = fibGenerator(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
