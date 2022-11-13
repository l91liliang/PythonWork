"""
homework21 - 写一个判断给定的正整数是不是质数的函数。

Author: larry
Date: 10/27/22

"""

from math import sqrt


def isPrime(num: int) -> bool:
    """
    判断一个正整数是不是质数

    :param num: 正整数
    :return: bool值，是否为质数
    """
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num != 1


n = int(input("请输入一个数："))
if isPrime(n):
    print(f"{n}是质数。")
else:
    print(f"{n}不是质数。")
