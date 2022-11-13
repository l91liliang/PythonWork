"""
example41 - 元组的应用

Author: larry
Date: 10/10/22

"""
a = (5, 10)#打包
print(a)
a, b = (5, 10)  # 赋值的过程实际上就是一个元组，写a,b=5,10也可
print(a)
print(b)
a, b, *c = 5, 10, 15, 20, 25  # 当有多个值赋给特定变量
print(a)
print(b)
print(c)
