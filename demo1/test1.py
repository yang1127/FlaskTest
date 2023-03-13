# -*-coding:utf-8-*-
from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def test1():
    # 数据库获取数据
    text = "YZQ"
    date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("test1.html", name=text, date=date_string)


# 测试锚点
@app.route("/test2")
def test2():
    return render_template("test2.html")


# 注册
@app.route("/test3")
def test3():
    return render_template("test3.html")


# @app.route("/do/ref")
# def test4():
#     # 1、接收用户信息
#     username = request.args.get("user")
#     password = request.args.get("pwd")
#     role = request.args.get("role")
#     gender = request.args.get("gender")
#     hobby_list =request.args.getlist("hobby")
#     print(username, password, role, gender, hobby_list)
#
#     # 2、将注册信息，放置数据库（后续）
#     # 将注册信息，放置本地文件中
#     with open('account.txt', mode='a', encoding='utf-8') as f:
#         line = "{}|{}|{}|{}|{}\n".format(username, password, role, gender, hobby_list)
#         f.write(line)
#
#     # 3、返回信息
#     return "success"


# 获取注册信息，注册成功
@app.route("/do/ref", methods=['POST'])
def test4():
    # 获取文件
    filename = request.files.get("files")
    filename.save('11.png')

    # 1、接收用户信息
    username = request.form.get("user")
    password = request.form.get("pwd")
    role = request.form.get("role")
    gender = request.form.get("gender")
    hobby_list =request.form.getlist("hobby")
    print(username, password, role, gender, hobby_list)

    # 2、将注册信息，放置数据库（后续）
    # 将注册信息，放置本地文件中
    with open('account.txt', mode='a', encoding='utf-8') as f:
        line = "{}|{}|{}|{}|{}\n".format(username, password, role, gender, hobby_list)
        f.write(line)

    # 3、返回信息，跳转到登录页面
    # return "success"
    return redirect("/login")


# 登录
@app.route("/login")
def test5():
    return render_template("test4.html")


# 获取登录信息，登录成功
@app.route("/do/login", methods=['POST'])
def test6():
    # 获取用户信息
    username = request.form.get("user")
    password = request.form.get("pwd")

    if username == "root" and password == "123":
        return "登录成功"
    else:
        return "登录失败"


if __name__ == '__main__':
    app.run()