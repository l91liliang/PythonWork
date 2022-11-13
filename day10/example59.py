"""
example59 - 字典的相关操作

Author: larry
Date: 10/19/22

"""
dict1 = {'A': 100, 'B': 200, 'C': 300}
dict2 = {'D': 400, 'E': 500, 'A': 600}

# dict3 = dict1 + dict2  # 字典之间不能作加法运算。
# print(dict3)

# 字典的更新与合并
dict1.update(dict2)
print(dict1)

# 删除元素
del dict1['B']  # 删除的指定键必须存在，不然会报错
dict1.pop('E')  # 删除的指定键必须存在，不然会报错
dict1.popitem()  # 默认删除字典中的最后一项
print(dict1)

# 清空所有键值对
dict1.clear()
print(dict1)

print('-' * 50)

# setdefault方法，如果这个键在字典中存在，setdefault返回原来与这个键对应的值，字典中原先的值不更新
# 如果这个键在字典中不存在，向字典中添加键值对，返回第二个参数的值，默认为None
dict1 = {'A': 100, 'B': 200, 'C': 300}
dict1.setdefault('C', 800)
dict1.setdefault('E', 10000)
print(dict1)
