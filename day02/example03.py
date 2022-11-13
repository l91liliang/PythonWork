"""

输入两个数据并进行加减乘除预算
Version：0.1
Author：Larry
Date：20220925
"""

# 变量-数据的载体
aq = int(input("请输入第一个数："))  # 需要类型转换
b = int(input("请输入第二个数："))  # 需要类型转换
print('%d+%d=%d' % (aq, b, aq + b))  # 表达方式，可以取代print(f"{aq}+{b}={aq + b}")
print(f"{aq}+{b}={aq + b}")
print(aq - b)
print(aq * b)
print(aq // b)  # 整除法（运算结果没有小数部分，不会四舍五入）
print(aq / b)
print(aq % b)
print(aq ** b)  # 求幂预算
