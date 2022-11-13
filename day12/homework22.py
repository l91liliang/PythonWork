"""
homework22 - 用函数实现求两个数的最大公约数和最小公倍数

写程序的终极原则：高内聚，低耦合--->high cohesion low coupling

设计函数最为重要的原则：单一职责原则（一个函数只做好一件事情）--->高度内聚
Author: larry
Date: 10/27/22

"""


# def gcd_and_lcm(x: int, y: int) -> int:
#     """求最大公约数和最小公倍数"""
#     a, b = x, y
#     while b % a != 0:
#         a, b = b % a, a
#     return a, x * y // a
# 以上函数功能太多。

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)


a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))
print(f'{a}和{b}的最大公约数是：{gcd(a, b)}，最小公倍数是：{lcm(a, b)}')
