# 高级特性
# python 代码讲究简洁
# 代码越少，开发效率越高

# 切片(Slice)
# 取一个list或tuple的部分元素是非常常见的操作
L = ['Mike', 'Jason', 'Jake', 'Newton']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。
# 即索引0，1，2
L[0:3]
# 如果第一个索引是0，还可以省略
# 所以等同于
L[:3]

# 倒数切片
# L[-3:]表示从倒数第三一直到最后
L[-3:]
# L[-3:-1]表示从倒数第三到倒数第一，不包括倒数第一
L[-3:-1]

# 间隔取数
# L[:10:2]前十个数每俩个取一个
L[:10:2]
# L[::3]所有数每三个取一个
L[::3]
# L[:]取所有数
L[:]

# 与list类似，tuple和字符串也可以使用切片
# 像tuple
(1, 2, 3, 4)[:3]
# 像字符串
'ABCDEF'[1:4]

# 在其他编程语言中，也会针对字符串定义截取函数substring
# 但在python中一个切片可以实现各种截取


# 迭代
# 通过for循环来遍历list或tuple，这种遍历称为迭代(Iteration)
# python的for循环可以迭代更多类型的对象相较于C(更强大)

# 像 list 和 tuple
L = ['Mark', 2, 'Scott']
for value in L:
    print(value)

Tup = ('Raj', 43, 12)
for value in Tup:
    print(value)

# 像 dict (字典也可迭代)
d = {'name': 'Jason', 'age': 22}
for key in d:
    print(key)
# 遍历 键值对中的值
for value in d.values():
    print(value)

# 像字符串也可以
str = 'what\' your education qualification?'
for val in str:
    pass

# 如何判断对象是否可迭代
# 通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable
# 判断整数对象能否迭代，答案是不行的(False)
isinstance(123, Iterable)

# 如何实现按下标迭代
# python 内置的 enumerate()函数来构造 元素-下标对
for i, value in enumerate(['I', 'You', 'We']):
    print(i, value)


# 列表生成式(List Comprehensions)
# 是Python内置的非常简单却强大的可以用来创建list的生成式

# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = [range(1, 11)]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 写列表生成式时，把要生成的元素 x * x 放到前面
# 后面跟for循环还可以加if判断
L = [x * x for x in range(1, 11)]
# 把满足if条件的元素输出
L = [x * x for x in range(1, 11) if x % 2 == 0]

# 还可以使用两层循环，可以生成全排列
# 生成 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
L = [x * x for x in 'ABC' for x in 'XYZ']

# 多变量循环
# for循环可以同时使用多个变量
# 比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in d.items():
    print(f'{key} = {value}')

# 所以list生成式也可以使用多变量
L = [f'{key} = {value}' for key, value in d.items()]

# 把一个list中的字母都变成小写
L = ['Mark', 'John', 'Scott']
l = [s.lower for s in L]

# if..else..
# 在列表表达式中，for后面的if是筛选条件，所以不能加else
# 在for前的if是表达式，所以必须加else，否则报错

L = [x if x % 2 == 0 else -x for x in range(1, 11) if x > 0]