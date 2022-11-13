"""
example40 - 元组--->不可变的容器，不可写。

元组是不可变类型,定义元组通常使用()字面量语法,元组类型支持的运算符跟列表是一样，元组的运行效率优于列表。

Author: larry
Date: 10/10/22

"""
fruits = ('apple', 'banana', 'grape')  # 三元组，元组中必须要有逗号。例如下面所示元组：
fruits_watermelon = ('watermelon',)
print(type(fruits))
print(type(fruits_watermelon))
# 重复运算
print(fruits * 3)
print('apple' in fruits)
print('grape' not in fruits)
# 合并运算
fruits2 = ('pitaya', 'litchi')
fruits3 = fruits + fruits2 + fruits_watermelon
print(fruits3)
# 索引和切片
print(fruits3[3])
print(fruits3[3:])

print(fruits3.index('apple'))
print(fruits3.count('apple'))
