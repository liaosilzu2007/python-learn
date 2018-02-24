import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

print("===============================")


def quadratic(a, b, c):
    return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a), (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

print("===============================")


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


s = "abcdea"
print(s[-1])
start = 0
end = 0
for i in range(len(s)):
    if s[i] != "a":
        start = i
        break
print(start)
for i in range(1, len(s) + 1):
    if s[-i] != "a":
        end = -i
        break
print(end)
print(s[start:end + 1])

for i in range(1, len(s) + 1):
    print(s[-i])


