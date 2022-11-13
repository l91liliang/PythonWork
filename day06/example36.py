"""
example36 - 冒泡排序法

效率比较低，元素两两比较，如果前面的元素大于后面的元素，就交换两个元素的位置
大的下去，小的上来。

[35，12，99，58，67，42，49，31，73]
[9,1,2,3,4,5,6,7,8]
[2,3,4,5,6,7,8,9,1]
Author: larry
Date: 10/8/22

"""
# nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]
nums = [9, 1, 2, 3, 4, 5, 6, 7, 8]  # 当用传统冒泡法时，效率非常低
for i in range(1, len(nums)):
    swapped = False  # 优化算法
    for j in range(0, len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True  # 优化算法
    if not swapped:  # 优化算法
        break  # 优化算法
print(nums)

nums1 = [2, 3, 4, 5, 6, 7, 8, 9, 1]  # 搅拌排序（鸡尾酒排序）