"""
example58 - 字典的运算

Author: larry
Date: 10/19/22

"""
student = {
    'id': 1001,
    'name': 'fmm',
    'sex': 'female',
    'birthday': '1994-01-14'
}

# 判断字典中有没有特定键
print('name' in student)
print('age' in student)
print('address' not in student)

# 在字典中，添加键值对或修改值。
student['address'] = 'wz'
student['id'] = 1005
print(student)
print('address' not in student)

# 使用get函数通过key获取value时，如果key不存在，不会发生KeyError错误，而是得到一个None（空值）
print(student.get('age'))
# 也可以将赋予没有的键一个默认的值
print(student.get('age', 20))
print(student)

# 删除键值对
# del student['name']#可以用del删
print(student.pop('name'))  # 也可用pop删
print(student.get('name', '无名氏'))
print(student)

# 如果要使用下标（索引）运算，那么必须要保证键一定存在
if 'birthday' in student:
    print(student['birthday'])
