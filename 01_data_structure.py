# input()函数用于输入信息
from unittest import result


name = input('Please enter your name:')

# print()函数用于打印信息
print('Hi,', name)
print('Hello, World!')
print('Hello,', 'World!')
print(200)
print(100 + 200)

'''
多行注释
多行注释
'''

"""
多行注释
多行注释
"""

# 数据类型
# 1.整型
num = -23   # 可以是负数
num = 0xff00    # 十六进制表示
num = 10_000_000    # 等同于 10000000 方便查看

# 2.浮点数
flt = 1.23
flt = 1.2e-5    # 科学计数法

# 3.字符串 
str = 'abc'
str = "xyz"    # 不区别单引号和双引号
str = '\t \n \\ \''    # \ 转义符号
str = r'\t\n'    # r'' 里的内容不转义

str = '''第一行
...第二行
...第三行'''    # '''...''' 格式表示换行输出，类似 \n

# 4.布尔值
bl = True
bl = False     # 布尔值 只有俩种
bl = True and False 
bl = True or False 
bl = not True    # 逻辑运算符 and, or, not

# 5.空值
empty = None    # python 表示空的特殊的值

# 变量
'''
python 属于动态语言，使用变量不需要声明
变量名只能以字母和_开头，不能用数字开头
并且区分大小写
'''
# 常量
# python 全大写变量名表示常量(其实还是变量)
GENDER = 'MAN'

# 运算符
# / 浮点数除法，结果一定是浮点数
res = 10 / 3
# // 地板除，结果一定是整数，就是把结果小数部分省略
res = 10 // 3
# % 取余运算，结果也一定是整数
res = 10 % 3