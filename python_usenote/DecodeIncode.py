# 报错信息：UnicodeDecodeError: ‘gbk’ codec can’t decode byte
# 报错误原因：Python 的 open 方法默认编码取决于平台，如果是 Windows 平台，默认编码是 gbk，如果文件是 utf-8 编码，就会报这个错误。
# 解决办法
'''
将打开文件的代码：

open(filename, 'r')

改为：

open(filename, 'r', encoding='utf-8')
'''

