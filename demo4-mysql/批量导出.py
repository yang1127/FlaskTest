# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor

# 导出：先操作数据库，再导出文件

# 1、数据库操作
# 连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
# 获取游标
cursor = conn.cursor(cursor=DictCursor)

# 查询
sql1 = "select * from t_admin"
cursor.execute(sql1)
data_list = cursor.fetchall()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

# 2、导出
for item in data_list:
    line = "{},{},{}\n".format(item['name'], item['password'], item['mobile'])
    with open("shuju.txt", mode='a', encoding='utf-8') as f:
        f.write(line)




