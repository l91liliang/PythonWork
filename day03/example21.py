"""
example21 - while循环，欧几里得算法、辗转相除法（与example的运算效率进行比较，大大提高）

原理：两个整数的最大公约数等于其中较小的数和两数相除余数的最大公约数。

Author: larry
Date: 10/3/22

"""
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))

while b % a != 0:
    temp = b
    b = a
    a = temp % a
    # a, b = b % a, a
print(a)
