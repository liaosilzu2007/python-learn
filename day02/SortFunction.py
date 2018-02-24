l = [36, 5, -12, 9, -21]
print(sorted(l))
print(sorted(l, key=abs))

l2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(l2))
print(sorted(l2, key=str.lower))
print(sorted(l2, key=str.lower, reverse=True))


