"""
example27 - 将一颗骰子掷60000次，统计每一面出现的次数。

升级版：将2颗骰子各掷60000次，统计每一面出现的次数。

Author: larry
Date: 10/5/22

"""

from random import randint as rand

# 一颗骰子版：
# D1 = 0
# D2 = 0
# D3 = 0
# D4 = 0
# D5 = 0
# D6 = 0
#
# for _ in range(60000):
#     temp = rand(1, 6)
#     if temp == 1:
#         D1 += 1
#     if temp == 2:
#         D2 += 1
#     if temp == 3:
#         D3 += 1
#     if temp == 4:
#         D4 += 1
#     if temp == 5:
#         D5 += 1
#     if temp == 6:
#         D6 += 1
#
# print(f"在60000次投骰子的过程中，1出现{D1}次，2出现{D2}次，3出现{D3}次，4出现{D4}次，5出现{D5}次，6出现{D6}次。")

# 两颗骰子版：
D1 = 0
D2 = 0
D3 = 0
D4 = 0
D5 = 0
D6 = 0
D7 = 0
D8 = 0
D9 = 0
D10 = 0
D11 = 0
D12 = 0

for _ in range(60000):
    temp = rand(1, 6) + rand(1, 6)
    if temp == 2:
        D2 += 1
    elif temp == 3:
        D3 += 1
    elif temp == 4:
        D4 += 1
    elif temp == 5:
        D5 += 1
    elif temp == 6:
        D6 += 1
    elif temp == 7:
        D7 += 1
    elif temp == 8:
        D8 += 1
    elif temp == 9:
        D9 += 1
    elif temp == 10:
        D10 += 1
    elif temp == 11:
        D11 += 1
    else:
        D12 += 1

print(
    f"在60000次投骰子的过程中，2出现{D2}次，3出现{D3}次，4出现{D4}次，5出现{D5}次，6出现{D6}次，7出现{D7}次，8出现{D8}次，9出现{D9}次，10出现{D10}次，11出现{D11}次，12出现{D12}次。")
# 以上语句太过于麻烦、复杂，并且还有可能要摇200颗骰子，所以此时需要使用容器型数据类型，示例件example30。
