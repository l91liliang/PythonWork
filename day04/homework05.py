"""
homework05 - 将一个不知道有多少位的正整数进行反转
如将123456转换为654321
Author: larry
Date: 10/3/22

"""
num = int(input("请输入一个整数："))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(f"翻转后的数字为：{reversed_num}。")
