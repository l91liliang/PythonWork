"""
example35 - 列表的相关操作，反转与排序

Author: larry
Date: 10/7/22

"""
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple', 'apple']
# 利用切片来打印倒转，但是原先的列表不变
print(items[::-1])
print(items)
# 真正反转列表
items.reverse()
print(items)

# 排序sort()
items.sort()  # 列表中元素按字母序排列，默认升序
print(items)
items.sort(reverse=True)  # 列表中元素按字母序降序
print(items)

nums = ['1', '10', '234', '2', '35', '100']  # 注意，列表中的数字为字符串
nums.sort()  # 按照字符串中的第一个数大小来排序，而不是按数字的实际大小来排。
print(nums)
nums2 = [int(num) for num in nums]  # 将字符串转换为整数后进行排序，即可用sort按照数字从小到大的顺序。
nums2.sort()
print(nums2)
nums.sort(key=int)  # key可以理解为需要比较的字符串的实际类型！！
print(nums)
