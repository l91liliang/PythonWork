"""
example45 - 字符串的操作（字符串的方法）

随时记住：字符串类型为不可变类型


Author: larry
Date: 10/15/22

"""
a = 'hello,world123'

# capitalize方法使字符串首字符大写
print(a.capitalize())
# upper方法使字符串的所有字符大写
print(a.upper())
# lower方法使字符串的所有字符小写
print(a.lower())
# title方法使字符串的每个单词字母大写
print(a.title())

# 判断字符串的属性
print(a.isdigit())  # 判断字符串是否全为数字
print(a.isalpha())  # 判断字符串是否全为字母
print(a.isalnum())  # 判断字符串是否为数字、字母构成
print(a.isascii())  # 判断字符串是否为ascii码构成
print(a.startswith('h'))  # 判断字符串是否以特定字母开头
print(a.endswith('3'))  # 判断字符串是否以特定字母结尾
