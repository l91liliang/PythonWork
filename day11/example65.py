"""
example65 - 定义和使用函数

计算组合数：C(M,N)=M!/N!/(M-N)!

Author: larry
Date: 10/25/22

"""

# def fac(M, N):
#     """
#     计算组合数。
#     fm:M的阶乘
#     fn:N的阶乘
#     fk:M-N的阶乘
#     :param M: M值
#     :param N: N值
#     :return: 计算出的组合数
#     """
#     fm = 1
#     for i in range(1, M + 1):
#         fm = fm * i
#     fn = 1
#     for j in range(1, N + 1):
#         fn = fn * j
#     fk = 1
#     for k in range(1, M - N + 1):
#         fk = fk * k
#     return fm / fn / fk


# 以上不用自己写，有相应模块：
from math import factorial as f

M = int(input("请输入M值："))
N = int(input("请输入N值："))
# print(f"组合数为：{int(fac(M, N))}")
print(f"组合数为：{int(f(M) / f(N) / f(M - N))}")
