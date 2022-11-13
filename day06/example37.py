"""
example37 - 列表应用的案例，随机抽样

Author: larry
Date: 10/9/22

"""
import random

nums = [i ** 2 for i in range(1, 99)]
print(len(nums))
print(random.sample(nums, 5))  # random.sample函数：无放回抽样，不可能抽到同一元素,抽出的是列表。
print(random.choices(nums, k=5))  # 有放回抽样，可能抽到同一元素,抽出的是列表。
print(random.choice(nums))  # 列表中随机抽取一个元素
random.shuffle(nums)  # 实现列表的随机乱序
print(nums)
