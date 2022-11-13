"""
example22 - 打印出1-100范围内的质数

Author: larry
Date: 10/4/22

"""
print("1-100中，以下数为质数：")
for a in range(2, 101):
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
    if is_prime:
        print(a, end=' ')
