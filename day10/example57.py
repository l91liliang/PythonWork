"""
example57 - 字典的创建和使用

Author: larry
Date: 10/19/22

"""

# 字面量语法（推荐）
student1 = {
    'id': 1001,
    'name': 'fmm',
    'sex': 'female',
    'birthday': '1994-01-14'
}
print(student1, len(student1))
for x in student1:
    print(x)  # 这样循环出来的是键。

for value in student1:
    print(student1[value])  # 这样循环出来的是值。

for key in student1:
    print(key, student1[key])  # 这样循环出来的是键-值对。

for value in student1.values():
    print(value)  # 这样循环出来的是值。

for key, value in student1.items():
    print(key, value)  # 这样循环出来的是键-值对。

# 构造器函数
student2 = dict(id=1002, name='larry', sex='male', birthday='1994-02-07')
print(student2)

# 生成式（推导式）语法
dict1 = {i: i ** 2 for i in range(1, 10)}
print(dict1)
