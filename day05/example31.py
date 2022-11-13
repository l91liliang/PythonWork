"""
example31 - 输入10个整数，计算平均值，方差和标准差，找出最大值和最小值

Author: larry
Date: 10/6/22

"""
import math

nums = []
sum = 0
var_nums = 0  # 方差
sd_nums = 0  # 标准差
for _ in range(10):  # 生成列表
    temp = int(input("请输入整数："))
    nums.append(temp)
for i in range(0, 10):  # 生成和
    sum += nums[i]
avg_nums = sum / 10  # 平均值
for i in range(0, 10):  # 方差
    var_nums += (nums[i] - avg_nums) ** 2 / 9

sd_nums = math.sqrt(var_nums)  # 标准差
min_num = nums[0]
max_num = nums[0]
for i in range(0, 10):
    if nums[i] < min_num:
        min_num = nums[i]
    if nums[i] > max_num:
        max_num = nums[i]

print(f"改组数的平均值为{avg_nums}，方差为{var_nums}，标准差为{sd_nums}，最大值为{max_num}，最小值为{min_num}。")
