"""
example70 - 高阶函数的用法（更加通用的函数）

Python中的函数是一等函数：
    1.函数可以作为函数的参数。
    2.函数可以作为函数的返回值。
    3.函数可以赋值给变量。

如果把函数作为函数的参数或者返回值，这通常被叫做高阶函数
通常使用高阶函数，可以实现对原有函数的解耦合操作。


Lambda函数--->没有名字而且一句话就能写完的函数。

Author: larry
Date: 10/30/22

"""
import operator


# *args--->可变参数--->可以接收零个或者任意多个位置参数
# **kwargs--->可以接收零个或任意多个关键字参数
# fn--->一个实现二元运算的函数（可以做任意二元运算）
def calc(fn, init_value, *args, **kwargs):
    total = init_value
    for arg in args:
        if type(arg) in (int, float):
            total = fn(total, arg)
    for value in kwargs:
        if type(value) in (int, float):
            total = fn(total, value)
    return total


# def add(x, y):
#     return x + y
#
#
# def mul(x, y):
#     return x * y
#
#
# def sub(x, y):
#     return x - y


print(calc(operator.add, 0, 11, 22, 33, 44))  # 可以从operator模块中导入方法
print(calc(operator.mul, 1, 11, 22, 33, 44))
print(calc(operator.sub, 0, 11, 22, 33, 44))
print(calc(lambda x, y: x * y, 1, 11, 22, 33, 44))  # lambda函数的用法，此句是乘法函数
