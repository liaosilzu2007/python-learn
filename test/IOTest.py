from io import StringIO
from io import BytesIO
import os


with open('D:/pycharm_workspace/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())


# 传'w'表示覆盖写，传'a'表示追加
with open('D:/pycharm_workspace/test.txt', 'w') as f:
    f.write('hello!\n')


print('===========================')
f = StringIO()
f.write('hello')
f.write('world!')
print(f.getvalue())
print('+++++++++++++++++++++++++++')
f1 = BytesIO()
f1.write('中文'.encode('utf-8'))
print(f1.getvalue())
f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f2.read())

print('+++++++++++++++++++++++++++++')
print(os.name)  # osix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.environ)
print(os.environ.get('PATH'))
print('=============================')
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，可以通过下面的方式
os.mkdir(os.path.join('d:/pycharm_workspace', 'testdir'))
# 删除一个目录
os.rmdir('d:/pycharm_workspace/testdir')

