"""
example09 - Python中的运算符
～赋值运算符（复合的赋值运算符）：右边的变量赋给左边 --->= += -= *= /= %= **=
~算术运算符--->+ - * / // % **
～关系运算符（比较运算符）---> > < >= <= == != 产生布尔值（True/False）
~逻辑运算符（重要）：把多个布尔值处理成一个布尔值（做多个布尔值的组合）---> and or not（与 或 非）


Author: larry
Date: 10/2/22

"""
# 赋值运算符（复合的赋值运算符）
print('赋值运算符：')
a = 5
print(a)
# a=a+3
a += 3
print(a)
# a=a-3
a -= 3
print(a)
# a=a*3
a *= 3
print(a)
# a=a/3
a /= 3
print(a)
# a=a%3
a %= 3
print(a)
# a=a**3
a **= 3
print(a)

# 关系运算符
print('关系运算符：')
print(a >= 7)
print(a >= 9)

# 逻辑运算符
print('逻辑运算符：')
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-' * 50)
print(True or False)
print(False or False)
print('-' * 50)
print(not False)
print(True and not False)
