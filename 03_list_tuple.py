#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
第一行注释是为了告诉Linux/OS X系统,这是一个Python可执行程序,Windows系统会忽略这个注释;

第二行注释是为了告诉Python解释器,按照UTF-8编码读取源代码,否则,你在源代码中写的中文输出可能会有乱码。
'''

# list 是python内置的数据类型

# list 元素没有类型要求
from sys import last_traceback


classmate = ['张三', '李四', 14, '王五']
# len()可以查看list元素个数
len(classmate)

# 按照索引访问元素，索引从0开始
# 第一个元素
print(classmate[0])
# 最后一个元素
print(classmate[len(classmate) - 1])
# 负号表示从后往前数
print(classmate[-1])

# list是一种有序的集合，可以随时添加和删除其中的元素。
# append()方法是在末尾追加元素
classmate.append('赵六')
# pop()方法是删除末尾的元素
classmate.pop()
# inert()方法把元素插到指定位置
classmate.insert(1, '赵六')
# pop()方法也可以删除指定位置
classmate.pop(1)
# 替换元素可以通过重新赋值
classmate[2] = '钱二'

# list 可以嵌套使用
s = [1, 2, 3]
l = [12, 13, s, 16]
# 等同于 
last_traceback = [12, 13, [1, 2, 3], 16]
# 访问方法,类似于 多维数组d
print(l[2][1])

# tuple 元组
# 元组一旦初始化不能修改

# () 用于定义元组
# 定义空元组
tup = ()
# 定义一个元素的元组，要加逗号消除和小括号的歧义
tup = (1, )
tup = (1, 2)

# 通过嵌套 list 实现 “可变的元组”
tup = ([1, 2], [3, 4])