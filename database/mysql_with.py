import pymysql
import contextlib

'''使用with简化mysql的连接过程，不用每次都要去关闭连接'''


# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host="119.23.246.206", port=3306, user="root", password="333000", db="java_test", charset='utf8'):
    connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        connection.commit()
        cursor.close()
        connection.close()


with mysql() as cur:
    print(cur)
    row_count = cur.execute('select * from book')
    row_1 = cur.fetchone()
    print('总记录条数：', row_count, '\n第一条记录：', row_1)
