"""
homework13 - 向列表中添加10个随机整数，找出其中第二大的元素。以及生成式的用法

Author: larry
Date: 10/6/22

"""
from random import randint

nums = [int(input("请输入数字：")) for _ in range(10)]  # 列表的生成式（推导式），省了非常多的语句！！！效率更高。
# 以下为简单选择排序算法

for i in range(0, 10):
    for j in range(i, 10):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)

for j in range(1, 9):  # 此段话是为了避免出现有多个最大值的情况
    if nums[0] == nums[j]:
        continue
    else:
        break
print(f"第二大的数为{nums[j]}。")
