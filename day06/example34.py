"""
example34 - 列表的相关操作

Author: larry
Date: 10/7/22

"""
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple', 'apple']

# 查找指定元素的索引位置（遇到的第一个）。没有相关元素的话，程序就会崩溃。
print(items.index('apple'))

# 查找指定元素的索引位置（从索引为3的元素之后寻找遇到的第一个）。没有相关元素的话，程序就会崩溃。
print(items.index('apple', 3))

# 查找相关元素出现的次数
print(items.count('apple'))

# 添加元素
items.append('blueberry')
items.insert(1, 'watermelon')
print(items)

# 删除元素
print(items.pop())  # pop函数可以返回被删除掉的值，pop()默认是删除掉最后一个元素。
items.pop(3)
print(items)
del items[0]  # 作用类似于pop，但是不会返回被删除的元素，不推荐使用
items.remove('apple')  # 删除列表中遇到的第一个apple
while 'apple' in items:
    items.remove('apple')  # 删除所有的apple
print(items)

# 清空列表元素
items.clear()
print(items)
