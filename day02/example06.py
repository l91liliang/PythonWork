"""
example06 - 格式化输出

Author: larry
Date: 2022/9/25

"""
aq = float(input("请输入第一个数："))  # 需要类型转换
b = float(input("请输入第二个数："))  # 需要类型转换
print('%f+%f=%f' % (aq, b, aq + b))  # 表达方式，可以取代print(f"{aq}+{b}={aq + b}")
print(f"{aq}+{b}={aq + b}")
print(aq - b)
print(aq * b)
print(aq // b)  # 整除法（运算结果没有小数部分，不会四舍五入）
print(aq / b)
print(aq % b)
print(aq ** b)  # 求幂预算
