"""
example29 - 列表的遍历（把每个元素依次取出来）

Author: larry
Date: 10/5/22

"""
nums = [35, 98, 12, 27, 66]
nums.append(91)
nums.append(22)
# print(nums)
# # 取第二个元素：
# print(nums[1])
# print(nums[-4])  # 即同一元素的列表索引值的绝对值必须要等于列表元素个数
#
# nums[2] = 120  # 列表的索引运算
# print(nums)

# 用循环取列表中的所有元素
for i in range(len(nums)):  # 通过len函数计算列表元素的个数，并以此控制循环变量的个数。既可读操作，又可写操作。
    print(nums[i])
print('-' * 20)
# 以下语句和上面的语句等效：
for num in nums:  # 只可读操作
    print(num)
print('-' * 20)
for i, num in enumerate(nums):  # 枚举方法
    print(i, num)  # 既取元素，又取序号
