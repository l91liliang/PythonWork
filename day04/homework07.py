"""
homework07 - 输入一个正整数，判断它是不是质数（只能被1和自身整除的数）

Author: larry
Date: 10/4/22

"""
a = int(input("请输入一个正整数："))
is_prime = True
if a <= 0:
    print("输入错误，请输入一个正整数。")
elif a == 1:
    print("1不是质数。")
else:
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime:
        print("该数为质数。")
    else:
        print("该数不是质数。")
