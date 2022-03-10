# for..in.. 结构
from tkinter import N


sum = 0
# for x in ... 循环就是把每个元素代入变量 X
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range()函数可以生成一个整数序列
# range()可以和 for循环搭配使用
for x in range(101):
    sum += x

# while.. 结构
n = 99
while n > 0:
    sum += n
    n -= 1

# break 语句
# 可以提前结束循环

# continue 语句
# 可以跳过当前循序剩下的语句

