"""
homework11 - 输入10个1-99的整数，并得出其中的平均数，最大值，最小值

Author: larry
Date: 10/5/22

"""
max_num = 1
min_num = 99
sum_num = 0
for _ in range(10):
    temp = int(input("请输入一个1-99之间的数："))
    if temp > max_num:
        max_num = temp
    if temp < min_num:
        min_num = temp
    sum_num += temp
print(f"这十个数的最大数为{max_num}，最小数为{min_num}，平均数为{sum_num / 10:.2f}。")
