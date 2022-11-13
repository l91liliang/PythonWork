"""
example18 - 求1-100之间3或5的倍数的和

Author: larry
Date: 10/3/22

"""
sum3 = 0
sum5 = 0
sum35 = 0
for i in range(3, 101, 3):
    sum3 += i
for j in range(5, 101, 5):
    sum5 += j
for k in range(1, 101):
    if k % 3 == 0 or k % 5 == 0:
        sum35 += k

print(f"在1-100之间，3倍数的和为{sum3}，5倍数的和为{sum5}，3或5倍数的和为{sum35}。")
