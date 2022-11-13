"""
example55 - 集合的操作（方法）

集合底层使用的是hash存储，通过计算元素的hash码来决定元素储存的位置，这是一种高效率的储存方案。
哈希存储的关键是设计一个好的hash函数，尽量保证不同的对象能够计算出不同的hash码。
可变容器（列表、集合、字典）都无法计算hash码，无法放入集合中。


Author: larry
Date: 10/18/22

"""
set1 = {'apple', 'banana', 'pitaya', 'apple'}
print(set1)

set2 = {True, False, False, False, True, True}
print(set2)

# TypeError: unhashable type: 'list'
# 集合中不可放入列表，集合底层使用了hash存储这种高效率的存储方式，而列表不支持此方式。
# set3 = {[1, 2, 3], [4, 5, 6]}
# print(set3)

# TypeError: unhashable type: 'set'
# set4 = {set1, set2}

list4 = [set1, set2]  # 集合可以放入列表中
print(list4)

set5 = {(1, 2, 3), (4, 5, 6)}  # 集合中可以放入元组
print(set5)

set1.add('grape')  # 向集合中添加元素
set1.add('durian')
print(set1)
set1.discard('apple')  # 在集合中删除特定元素
print(set1)
deleted_elem = set1.pop()  # 在集合中随机删除元素，被删除的元素可以返回。
print(set1, deleted_elem)

set6 = frozenset({1, 3, 5, 7})  # 不可变集合
print(set6)

# 通过列表构造集合
nums = [1, 1, 1, 10, 1, 0, 5, 3, 9, 8, 9]
set7 = set(nums)
print(set7)

# 将集合转换为列表
list5 = list(set7)
print(list5)
