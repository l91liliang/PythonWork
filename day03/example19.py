"""
example19 - 输入两个正整数，找出它们的最大公约数

Author: larry
Date: 10/3/22

"""
a = int(input("输入第一个正整数："))
b = int(input("输入第二个正整数："))
c = min(a, b)
for i in range(c, 0, -1):
    if a % i == 0 and b % i == 0:
        print(f"最大公约数为：{i}")
        break
