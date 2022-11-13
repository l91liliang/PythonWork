"""
example17 - 实现1-100求和

Author: larry
Date: 10/3/22

"""
# 方法1
total = 0
for x in range(1, 101):
    total += x
print(total)

# 方法2
print(sum(range(1, 101)))
