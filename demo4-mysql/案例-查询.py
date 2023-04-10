# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor

while True:
    name = input("输入要查询的用户名：")

    # 连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
    # 获取游标
    cursor = conn.cursor(cursor=DictCursor)

    # 查询
    sql1 = "select * from t_admin where name=%s"
    cursor.execute(sql1, [name])
    # result = cursor.fetchall()
    # print(result)

    # fetchone() 为空，返回null
    result = cursor.fetchone()
    print(result)

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()

