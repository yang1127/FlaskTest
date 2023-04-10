# -*-coding:utf-8-*-
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
# 获取游标
cursor = conn.cursor()


# 创建表
sql = """
create table t_admin(
    id int not null auto_increment primary key,
    name varchar(16) not null,
    password varchar(16) not null,
    mobile char(11) not null
)default charset=utf8;
"""
cursor.execute(sql)
conn.commit()


# 关闭游标
cursor.close()

# 关闭连接
conn.close()