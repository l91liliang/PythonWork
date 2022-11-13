"""
homework12 - 输入三个整数，按从大到小的顺序进行输出。

Author: larry
Date: 10/6/22

"""
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

print(f"排序为{a}>{b}>{c}。")
