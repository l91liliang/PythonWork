"""
homework10 - 猜数字游戏

计算机产生一个1-100的随机数，人输入自己猜的数字，
计算机给出对应的提示"大一点"、"小一点"或"恭喜你猜对了"，直到猜中为止。
如果猜的次数超过7次，计算机温馨提示"智商余额明显不足"。

Author: larry
Date: 10/5/22

"""
from random import randint as rand

num = rand(1, 100)
# print(num)
i = 0
while True:
    i += 1
    a = int(input("请输入您猜的数字："))
    if a > num:
        print("小一点")
        if i > 7:
            print("智商余额明显不足")
            break
    elif a < num:
        print("大一点")
        if i > 7:
            print("智商余额明显不足")
            break
    else:
        print(f"恭喜您使用{i}次答对了。")
        break
