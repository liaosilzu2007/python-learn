import pymysql

connection = pymysql.connect(host="119.23.246.206", port=3306, user="root", password="333000",
                             db="java_test", charset='utf8')  # 指定字符集避免中文乱码
cur = connection.cursor()

'''查询'''
# select_sql = 'select * from book'
# try:
#     # 查询所有记录
#     cur.execute(select_sql)
#     results = cur.fetchall()  # 查询出所有记录，如果要查询10条记录，使用fetchmany(10)方法
#     for row in results:
#         bookId = row[0]
#         bookName = row[1]
#         author = row[2]
#         price = row[3]
#         print(bookId, '----', bookName, '----', author, '----', price)
#
#     # 查询前10条记录
#     cur.execute(select_sql)
#     results2 = cur.fetchmany(10)
#     print(results2)
# except Exception as e:
#     raise e
# finally:
#     cur.close()
#     connection.close()


'''更新'''
update_sql = 'update book set price = %d where id = %d'
try:
    # 使用占位符的方式可以防止sql注入
    effect_rows = cur.execute(update_sql % (59.5, 1))

    # 需要commit之后才能真正更新数据库
    connection.commit()

    # 打印受影响的行数，如果更新的新数据和原来的数据是一样的，则受影响的行数为0
    print(effect_rows, 'rows are effected')
except Exception as e:
    connection.rollback()
    raise e
finally:
    cur.close()
    connection.close()

