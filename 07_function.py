# function 函数
# 函数要求传入参数数量匹配，否则报错
# abs() 绝对值函数
print(abs(-39))

# 数据类型转换函数
int('123')
float(12)
str(1.21)
bool(1)

# 函数名就是指向函数对象的引用
a = abs
a(-1)

# 函数定义
def my_abs(x):
    if(x > 0):
        return x
    else:
        return -x


# 表示从 abstest.py 文件中引入 my_abs()函数
'''from abstest import my_abs'''

# 定义一个空函数
# pass 是一个占位符，表示这里先空着
def nop():
    pass

# 类似的
if(a > 1):
    pass

# 参数类型错误时，一般需要处理错误
# 以后细讲

# 函数返回多值
# 表示引入math包
import math
# angle = 0 表示默认值
# 必选参数在前，默认参数在后
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 多值返回其实本质是返回一个 tuple，可以用多个变量接住
x, y = move(100, 100, math.pi / 6)

# 有多个默认参数时，既可以按顺序默认传值
def prints(city = 'jiaxing', school = 'nanhu', major = 'network'):
    print(city)
    print(school)
    print(major)

# 也可以加默认参数名，实现不按顺序传值
prints(major = 'computer sciences')

# 函数默认参数一定要是不变对象
# 避免 默认参数 = []

# 可变参数
# 可变参数就是传入的参数个数是可变的
# 参数前带 * ，可以让传入的参数变成一个tuple
def calc(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

# 当需要把list或tuple作为可变参数传入时
# 只要在变量名前加 * ，自动转化成可变参数
nums = [1, 2, 3, 4]
calc(*nums)

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

# 参数前加俩个 * ，表示关键字参数
# 接收任意个带参数名的参数，组成字典
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 注意写法： city = 'jiaxing'
person('Jason', 22, city='jiaxing')

# 关键字参数也可以直接传一个字典变量
extra = {'city': 'jiaxing', 'school': 'nanhu'}
# 字典前加俩个 * ，表示关键字参数   
person('Jason', 22, **extra)

# 命名关键字参数
# 用以限制传入指定的关键字参数

# 在 * 后面的就是 命名关键字参数
# 命名关键字参数也可以默认
def person(name, age, *, city='jiaxing', school):
    print(name, school)

# * 是分隔符，如果有可变参数，则可以省略 *
def person(name, *args, city, school):
    pass

# 命名关键字参数必须加参数名
person('Mike', 44, city='shanghai', school='fudan')
person('Raj', 31, school='MIT')

# 总结
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def demonstrate(a, b=0, *c, d, **e):
    pass

# 实际中不会有这么复杂的参数组合，但是需要会写
# 另外，对于任意函数，都可以通过类似 func(*args, **kw)的形式调用它，无论它的参数是如何定义的

args = (1, 2, 3, 4)
kw = {'name': 'Jake', 'age': 22}

demonstrate(*args, **kw)