"""
example06 - 格式化输出

Author: larry
Date: 2022/9/25

"""
aq = float(input("请输入第一个数："))  # 需要类型转换
b = float(input("请输入第二个数："))  # 需要类型转换
print('%.2f+%.2f=%.2f' % (aq, b, aq + b))  # 表达方式，与下方语句等价
print(f"{aq:.2f}+{b:.2f}={aq + b:.2f}")  # 格式化输出的便捷语法
