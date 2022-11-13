"""
homework06 - 输入两个非负整数m和n（m>=n），计算C(m,n)的值
A(m,n)=m!/(m-n)!--->排列--->permutation
C(m,n)=m!/n!/(m-n)!--->组合--->combination

Author: larry
Date: 10/3/22

"""
import math  # 简便算法

m = int(input("请输入非负整数m="))
n = int(input("请输入非负整数n="))
# 以下为用循环语句计算的办法，为本节所学内容。实际上导入math的求阶乘模块即可计算。
# factorial_m = 1
# factorial_n = 1
# factorial_m_reduce_n = 1
# if m < n:
#     print("错误，请重新输入，m要大于n。")
# if m >= n:
#     for i in range(m, 0, -1):
#         factorial_m = factorial_m * i
#     for j in range(n, 0, -1):
#         factorial_n = factorial_n * j
#     for k in range(m - n, 0, -1):
#         factorial_m_reduce_n = factorial_m_reduce_n * k
#     cmn = factorial_m / factorial_n / factorial_m_reduce_n
#     print(f"C(m,n)={cmn:.0f}")

print(math.factorial(m) // math.factorial(n) // math.factorial(m - n))
