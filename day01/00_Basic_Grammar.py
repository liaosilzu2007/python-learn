import sys

# ================基本语法================
# python中语句结尾不需要有标点符号。

# 1.多行语句
# Python语句中一般以新行作为语句的结束符，但也可以使用斜杠（\）将一行的语句分为多行显示
item_one = 'item_one'
item_two = 'item_two'
item_three = 'item_three'
total = item_one + \
        item_two + \
        item_three

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


# 2.引号
# Python中可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 3.注释
# 单行注释使用‘#’号，多行注释使用三个单引号 ''' 或三个双引号 """。
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 4.同一行多条语句
# 每条语句用分号分隔
line_item_1 = "line_item_1";line_item2 = "line_item2";print(line_item_1 + "," + line_item2)

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
