"""
example46 - 字符串的操作
在字符串中查找有没有某个子串
-index/rindex
-find/rfind
字符串--->string
子串--->substring

Author: larry
Date: 10/15/22

"""
a = 'Oh apple, i love apple.'
# index--->从左向右寻找指定的子串，可以指定从哪开始找，默认是0。可以添加一个参数，指定从某一位开始找。
# 找到了返回子串对应的索引，找不到直接报错。
print(a.index('apple'))  # 从左往右返回索引
print(a.index('apple', 10))
print(a.rindex('apple'))  # 从右往左返回索引
# ValueError: substring not found
# print(a.index('banana'))

# find用法比index更稳定，不会崩溃。
print(a.find('apple'))  # 从左往右返回索引
print(a.find('apple', 10))
print(a.rfind('apple'))  # 从右往左返回索引
print(a.find('banana'))  # 如果字符串中没有对应子串的话，不会崩溃，会返回-1
