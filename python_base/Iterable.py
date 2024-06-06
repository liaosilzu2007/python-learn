from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print('===================')

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))


