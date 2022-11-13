"""
example10 - 逻辑运算的应用 判断整数a是不是大于50的偶数

and 和 or两个运算符具有短路功能，因此也被称为短路运算符
Author: larry
Date: 10/2/22

"""
a = int(input('a='))
flag1 = a > 50
flag2 = a % 2 == 0
print(flag1, flag2)
print(flag1 and flag2)
