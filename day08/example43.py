"""
example43 - 字符串的运算

注意：字符串也是不变数据类型，只能进行读操作，不能进行改写操作！！！

Author: larry
Date: 10/15/22

"""
# 字符串的重复运算
a = 'hello,world'
print(a * 5)

# 获取字符串的长度
print(len(a))

# 循环遍历字符串每个字符
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

# 成员运算，判断特定字符串是否在字符串中。
print('or' in a)
b = 'hello,World'

# 比较运算
print(a == b)
print(a != b)

c = 'goodbye,world'
print(b > c)
