# 生成器(generator)
# 是一种一边循环一边计算的机制

# 生成器表达式
# 区别与列表表达式，外面是 ()
g = (x * x for x in range(10))

# list 列表可以直接打印每一个元素
# 生成器通过next()访问每一个元素 
next(g)

# 一直手动调用next()不现实
# 生成器也是可迭代对象，可以使用for循环迭代
for x in g:
    print(x)

# 用函数实现打印斐波那契数列
def fib(max):
    # 多值赋值
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # 核心实现代码
        a, b = b, a + b
        n = n + 1
    return 'done'

# 其实fib()函数就是定义一种推算规则
# 这种函数与generator很像
# 把fib()变成generator只需要把print变成yield就可以
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

# 区别就是generator函数和普通函数的执行流程不一样
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# generator函数每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# 调用generator函数会创建一个generator对象
o = odd()
next(o) # 1
next(o) # 3
next(o) # 5

# 多次调用generator函数会创建多个相互独立的generatoro = odd()
next(odd()) # 1
next(odd()) # 1
next(odd()) # 1

# 实际操作中，不会使用next()函数调用
# 一般使用循环迭代generator对象
g = fib(6)
# 错误处理机制，以后再说
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 总结
# 生成器有简短的生成器表达式形式
# 也有更强大的生成器函数的形式