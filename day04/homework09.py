"""
homework09 - 找出1-10000之间的完美数（除自身外所有因子的和)等于这个数

Author: larry
Date: 10/4/22

"""
import time

start_time = time.time()

# 低效算法，效率低
# for i in range(1, 10001):
# sum = 0
# for j in range(1, i + 1):
#     if i % j == 0:
#         sum += j

# 普通算法，效率一般
# for i in range(1, 10001):
# sum = 0
# for j in range(1, int(i / 2) + 1):
#     if i % j == 0:
#         sum += j

# 高效算法，效率高
for i in range(2, 10001):
    sum = 1
    for j in range(2, int(i ** 0.5) + 1):  # 原理：https://blog.csdn.net/ningmengshuxiawo/article/details/106988903
        if i % j == 0:
            sum += j
            if j != i // j:
                sum += i // j

    if sum == i:
        print(f"{i}是完美数。")
end_time = time.time()
print(f"执行时间：{end_time - start_time:.3f}s")
