"""
homework04 - 100-999之间的水仙花数
如153=1^3+5^3+3^3

Author: larry
Date: 10/3/22

"""
for i in range(100, 1000):
    a = int(i / 100) ** 3  # 用整除更好 a=i//100 整除：相除后，取商。
    b = int(i % 100 / 10) ** 3  # 用整除更好 b=i//10%10
    c = int(i % 10) ** 3
    d = a + b + c
    if i == d:
        print(i)
