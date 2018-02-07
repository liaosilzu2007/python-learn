import sys

myList = ["taobao", "jingdong", "suning", "dangdang"]
for ele in myList:
    if ele == "suning":
        print("跳出循环！")
        break
    print(ele)

print("===============")

for idx in range(len(myList)):
    print(idx, myList[idx])

print("===============")

for i, j in enumerate(myList):
    print(i, j)

print("===============")

for i in range(100, 102):
    print(i)

it = iter(myList)
print(next(it))
print(next(it))
# for x in it:
#     print(x, end=";")

print("\n===============")

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
