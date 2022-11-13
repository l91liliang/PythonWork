"""
homework16 -有一个放整数的列表，找出列表汇总出现次数最多的元素。

Author: larry
Date: 10/15/22

"""
import random

items = [random.randint(1, 10) for _ in range(100)]
print(items)
max_items, max_counter = [items[0]], items.count(items[0])

for item in items:
    curr_counter = items.count(item)
    if curr_counter > max_counter:
        max_items.clear()
        max_items.append(item)
        max_counter = curr_counter
    elif curr_counter == max_counter:  # 避免出现不同元素出现相同次数的情况。
        if item not in max_items:
            max_items.append(item)

for max_item in max_items:
    print(f"{max_item}出现次数最多，出现了{max_counter}次。")
