"""
example30 - 摇N颗骰子，计算掷600000次后，每种组合出现的次数。

Author: larry
Date: 10/6/22

"""
from random import randint as rand

N = int(input("请输入你要掷几颗骰子："))
Ds = [0] * 6 * N
for _ in range(600000):
    temp = 0
    for _ in range(N):
        temp += rand(1, 6)
    Ds[temp - N] += 1
for i in range(N * 1, N * 6 + 1, 1):
    print(f"{i}出现{Ds[i - N]}次", end='\n')
