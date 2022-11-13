"""
homework15 - 一个列表中有很多重复元素，写一段代码去掉列表中的重复元素。

Author: larry
Date: 10/15/22

"""
import random

items = [random.randint(1, 11) for _ in range(100)]
print(items)
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)
