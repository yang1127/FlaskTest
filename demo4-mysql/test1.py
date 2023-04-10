# -*-coding:utf-8-*-
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
# 获取游标
cursor = conn.cursor()

'''
# 创建表
sql = """
create table t_yzqtest(
    id int not null auto_increment primary key,
    name varchar(16),
    mobile char(11),
    salary decimal(10, 2)
)default charset=utf8;
"""
cursor.execute(sql)
conn.commit()
'''

# 插入
sql1 = "insert into t_yzqtest(id, name, mobile, salary) values(2, 'yzq', 18702970462, 1000)," \
       "(3, 'yzq', 18702970463, 2000)," \
       "(4, 'yzq', 18702970464, 3000)"
cursor.execute(sql1)
conn.commit()



# 删除
sql2 = "delete from t_yzqtest where id=1"
cursor.execute(sql2)
conn.commit()



# 查询
sql3 = "select id, name, mobile, salary from t_yzqtest;"
# 执行sql语句
cursor.execute(sql3)
# 获取结果
result3 = cursor.fetchall()
print(result3)


# 修改
sql4 = "update t_yzqtest set name='杨芝琪' where id=3"
cursor.execute(sql4)
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

