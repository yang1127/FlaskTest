# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/home')
def home():
    # 连接pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
    # 获取游标-DictCursor以字典形式返回
    cursor = conn.cursor(cursor=DictCursor)

    cursor.execute("select id, name, password, mobile from t_admin")
    data_list = cursor.fetchall()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return render_template("home.html", data_list=data_list)


@app.route('/admin/delete')
def delete():
    # 拿到要删除的用户id
    id = request.args.get('id')
    # print(id)
    # return "success"

    # 在数据库中删除该用户
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
    # 获取游标
    cursor = conn.cursor(cursor=DictCursor)

    # 删除
    sql = "delete from t_admin where id=%s;"
    cursor.execute(sql, [id])
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return redirect("/home")


# 法一
# @app.route('/admin/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     # 连接pymysql
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
#     # 获取游标-DictCursor以字典形式返回
#     cursor = conn.cursor(cursor=DictCursor)
#
#     cursor.execute("select * from t_admin where id=%s", id)
#     user = cursor.fetchone()
#     # print(user)
#
#     if request.method == 'POST':
#         name = request.form['name']
#         password = request.form['password']
#         mobile = request.form['mobile']
#
#         cursor.execute('UPDATE t_admin SET name=%s, password=%s, mobile=%s WHERE id=%s', (name, password, mobile, id))
#         conn.commit()
#
#         return redirect('/home')
#
#     # 关闭游标
#     cursor.close()
#
#     # 关闭连接
#     conn.close()
#
#     return render_template("edit.html", user=user)

# 法二
@app.route('/admin/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    print(id)
    # 连接pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yyy1536520643', database="books")
    # 获取游标-DictCursor以字典形式返回
    cursor = conn.cursor(cursor=DictCursor)

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        mobile = request.form.get('mobile')

        cursor.execute('UPDATE t_admin SET name=%s, password=%s, mobile=%s WHERE id=%s', (name, password, mobile, id))
        conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()

    return redirect("/home")


if __name__ == '__main__':
    app.run()
