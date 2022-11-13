"""
example53 - 集合的定义

Author: larry
Date: 10/17/22

"""

set1 = {1, 2, 3, 3, 3, 2}  # 集合中的元素具有无序性、互异性、确定性
print(set1, len(set1))  # 集合的互异性（没有重复元素）
set2 = set()  # 创建空集合的方法。不能用set2={}，这样创建的是空字典。

# 集合的无序性
# TypeError: 'set' object is not subscriptable
# print(set1[0])

# 遍历集合中的元素
for elem in set1:
    print(elem)
