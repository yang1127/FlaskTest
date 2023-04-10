# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor

while True:
    print("修改密码：")
    name = input("输入用户名：")
    password = input("修改后密码：")

    # 连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
    # 获取游标
    cursor = conn.cursor(cursor=DictCursor)

    # 修改
    sql1 = "update t_admin set password=%s where name=%s"
    cursor.execute(sql1, [password, name])
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()
