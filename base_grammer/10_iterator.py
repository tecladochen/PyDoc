# 迭代器 Iterator
# 把直接可以用for循环迭代的对象称为Iterable
# 可迭代对象
# 第一类 list，tuple，dict，set
# 第二类 generator生成器

# 把可以调用next()函数的对象称为迭代器(Iterator)
# generator是迭代器的一种
# 
# terator对象可以调用next()并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 所以Iterator甚至可以表示一个无限大的数据流