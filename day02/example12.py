"""
example12 - 输入三角形的三条边长度，判断能否构成三角形

规则：任意两边的长度和大于第三边

Author: larry
Date: 10/2/22

"""
print('输入三角形三条边的长度：')
a = int(input('a='))  # 注意一定要转换为数字
b = int(input('b='))  # 注意一定要转换为数字
c = int(input('c='))  # 注意一定要转换为数字
flag1 = (a + b) > c
flag2 = (b + c) > a
flag3 = (a + c) > b
print(flag1)
print(flag2)
print(flag3)
print(flag1 and flag2 and flag3)
