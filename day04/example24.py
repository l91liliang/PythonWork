"""
example24 - 乘法口诀表

Author: larry
Date: 10/4/22

"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end='\t')
    print("")
