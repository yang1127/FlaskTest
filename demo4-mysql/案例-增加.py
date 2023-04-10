# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor

while True:
    name = input("用户名：")
    password = input("密码：")
    mobile = input("手机号：")

    # 连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
    # 获取游标
    cursor = conn.cursor(cursor=DictCursor)

    # 插入
    sql1 = "insert into t_admin(name, password, mobile) values(%s, %s, %s);"
    cursor.execute(sql1, [name, password, mobile])
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()



