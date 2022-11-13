"""
example23 - 输入N，按照如下所示的规律进行打印。
N=5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Author: larry
Date: 10/4/22

"""
N = int(input("请输入一个正整数："))
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print("")
