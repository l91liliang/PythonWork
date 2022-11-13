"""
example69 - 在设计函数的时候，函数的参数个数是暂时无法确定的

Author: larry
Date: 10/30/22

"""


# *args--->可变参数--->可以接收零个或者任意多个位置参数
# **kwargs--->可以接收零个或任意多个关键字参数
def add(*args, **kwargs):  # 加*号就打包了，可以打包成元组 ||||| 加**号就打包了，可以打包成字典。
    print(args, type(args))
    print(kwargs, type(kwargs))
    # return sum(args)
    total = 0
    for arg in args:
        if type(arg) in (int, float):
            total += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            total += value
    return total


def mul(*args, **kwargs):  # 加*号就打包了，可以打包成元组 ||||| 加**号就打包了，可以打包成字典。
    print(args, type(args))
    print(kwargs, type(kwargs))
    # return sum(args)
    total = 1
    for arg in args:
        if type(arg) in (int, float):
            total *= arg
    for value in kwargs.values():
        if type(value) in (int, float):
            total *= value
    return total


print(add(1))
print(add(1, 2, 3, 4, 'hello'))
print(add(1, 2, a=3, b=4, c='hello'))
print(add(1, 8, 8, 6))

# 以下语句会引发TypeError错误：
# print(add(a=1, b=8, c=8, d=6))


print(mul(1, 8, 8, 6))
