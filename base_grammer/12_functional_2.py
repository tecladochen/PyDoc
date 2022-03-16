# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 4)
# 调用函数求值
f()

# 闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 一定要用可以再次嵌套函数
# 使用闭包，就是内层函数引用了外层函数的局部变量

def inc():
    x = 0
    def fn():
        # 可以调用外层变量
        # 使用闭包时，对外层变量赋值前
        # 需要先使用nonlocal声明该变量不是当前函数的局部变量
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1


# 匿名函数(lambda 函数)
list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
# lambda x: x * x 
# 等同于
# 只是这个函数没有名字
def f(x):
    return x * x
# 匿名函数可以作为值返回
def build(x, y):
    return lambda: x * x + y * y

# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数

# 装饰器(decorator)

# 偏函数(Partial function)
import functools
int2 = functools.partial(int, base = 2)
int2('1010011101')
# 当函数的参数个数太多，需要简化时
# 使用functools.partial可以创建一个新的函数
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单