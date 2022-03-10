# dict 字典(在其他语言中叫 map)
# 使用键值对存储，具有很快的查询速度
d = {'Mike': 93, 'John': 100, 'Marry': 98}

# 访问元素方式
print(d['John'])
# 判断key值是否存在
print('John' in d)
# pop(key)可以删除一个键值对
d.pop('Mike')


# set 集合(数学概念上的集合)
# set 是key的集合，所以不能有重复
# 要创建一个set，必须以一个list作为参数
s = set([1, 2, 3])

# add()向集合添加一个key
s.add(4)
# remove()向集合删除一个key
s.remove(3)

# 集合运算
s1 = set([3, 4, 5])
s2 = set([1, 2, 3])
# & 表示俩个集合做交集
s1 & s2
# | 表示俩个集合做并集
s1 | s2

# set和dict的唯一区别仅在于没有存储对应的value