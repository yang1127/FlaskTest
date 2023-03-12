# -*-coding:utf-8-*-
# # 1、基本用法
# # 1.1 按照{}的顺序依次匹配括号中的值
# s1 = "{} is a {}".format('Tom', 'Boy')
# print(s1)  # Tom is a Boy
#
# # s2 = "{} is a {}".format('Tom')
# # print(s2)  # 报错，IndexError: Replacement index 1 out of range for positional args tuple
#
# # 1.2 通过索引方式去匹配参数
# # 注意：索引和默认格式会报错，如：s3 = "{} is a {1}".format('Tom', 'Boy')
# s3 = "{0} is a {1}".format('Tom', 'Boy')
# print(s3)  # Tom is a Boy
#
# s4 = "{2} is a {1}".format('Tom', 'Boy', 'Girl', 'XiXi')
# print(s4)  # Girl is a Boy
#
# # 1.3 通过参数名来匹配参数
# s5 = "{name} is {age} years old".format(name="Tom", age=10)
# print(s5)  # Tom is 10 years old
#
# # 1.4 混合应用，注意：命名参数必须写在最后，如例子中，age=10
# s6 = "My name is {}, i am {age} year old, She name is {}".format('Liming', 'Lily', age=10)
# print(s6)  # My name is Liming, i am 10 year old, She name is Lily

# 2、高阶用法
# 2.1 通过对象属性
class Names():
    name1 = 'Tom'
    name2 = 'XiXi'


print('Hello {names.name1}, i am {names.name2}'.format(names=Names))  # Hello Tom, i am XiXi


# 2.2 支持参数部分引用
s7 = "The word is {s}, {s[0]} is initials".format(s='world')
print(s7)  # The word is world, w is initials

# 2.3 数字处理
# 保留小数位
s8 = 'π is %.2f'% 3.1415926
print(s8)  # π is 3.14

s9 = 'π is {:.2f}'.format(3.1415926)
print(s9)  # π is 3.14

# 转换进制 b-二进制、o-八进制、X-十六进制
s10 = '{:b}'.format(8)
print(s10)

#2.3 格式处理
# 1）+数字指定转换后的字符串长度，不足的部分用空格补充
# 2）如果指定的长度小于参数的长度，按照原参数匹配
s11 = '{:2}b'.format('a')
print(s11)  # a b

s12 = '{:2}world'.format('hello')
print(s12)  # helloworld


# 2.3 字符的填充
# 1）符号^数字进行字符串的填充，其中数字为填充后的字符串总长度
# 2）如果数字小于字符串的长度，则不进行填充操作
s13 = '{:*^10}'.format('hello')
print(s13)  # **hello***

s14 = '{:*^2}'.format('hello')
print(s14)  # hello

# 2.4 list和tuple的拆分
# 在format格式化时，可使用* 或者 ** 进行对list、tuple拆分
s15 = ['test1', 'test2', 'test3']
s16 = 'i like {} and {} and {}'.format(*s15)
print(s16)  # i like test1 and test2 and test3

s17 = 'i like {0} and {1} and {2}'.format(*s15)
print(s17)  # i like test1 and test2 and test3

# 字典需要**拆分
dict18 = {'name': 'yzq', 'age': 18}
s17 = 'My name is {name}, i am {age} years old'.format(**dict18)
print(s17)  # My name is yzq, i am 18 years old




