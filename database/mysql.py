import pymysql

db = pymysql.connect(host="119.23.246.206", port=3306, user="root", password="333000",
                     db="java_test", charset='utf8')  # 指定字符集避免中文乱码
cur = db.cursor()

sql = 'select * from book'
try:
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        bookId = row[0]
        bookName = row[1]
        author = row[2]
        price = row[3]
        print(bookId, '----', bookName, '----', author, '----', price)
except Exception as e:
    raise e
finally:
    db.close()
