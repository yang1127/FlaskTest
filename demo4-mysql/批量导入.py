# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor

with open('account.txt', mode='r', encoding='utf-8') as f:
    # 读取每一行数据
    for line in f:
        # 每一行以换行结尾
        line = line.strip()
        if not line:
            continue
        data_list = line.split("|")

        # 连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
        # 获取游标
        cursor = conn.cursor(cursor=DictCursor)

        # 插入
        sql1 = "insert into t_admin(name, password, mobile) values(%s, %s, %s);"
        cursor.execute(sql1, data_list)
        conn.commit()

        # 关闭游标
        cursor.close()

        # 关闭连接
        conn.close()




