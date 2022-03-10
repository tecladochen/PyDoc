#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 字符和编码
# ord()获取字符的整数表示
ord('A')

# chr()把编码转换成字符
chr(96)

# len()函数计算字符串的字符数
len('Jason')

# 格式化
# 风格与C语言类似
str = 'Hello, %s' % 'World!'
# 当有多个替换时，要加括号
str = 'Hi, %s, my name is %s' % ('Jason', 'Raj')
'''
%d      整数
%02d    表示这个整数用2位表示,并且前面补0

%f      浮点数
%.2f    表示保留俩位小数

%s      字符串(可以把任何类型转换成字符串输出)

%x      十六进制数

%%      用来转义%
'''
# 另一种格式化方式
# format()函数,不如 % 好用
str = 'Hi, {0}, 你的成绩是 {1}'.format('小明', 100)

# f-string 字符串
# 在f''中{}中的变量名会直接替换
name = 'Lilei'
age = 19
str = f'Hi, {name}, your age is {age}.'
