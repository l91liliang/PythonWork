"""
example16 - 输出十次hello,world（循环结构）

Author: larry
Date: 10/3/22

"""
# 以下句子的结果一致
# while结构

# for-in循环结构（适用于不知道要循环多少次）
for i in range(10):  # i从0循环到9
    print(i, "Hello, world!")

print('-' * 50)

for i in range(0, 10):  # i从0循环到9，即[0,10)
    print(i, "Hello, world!")
