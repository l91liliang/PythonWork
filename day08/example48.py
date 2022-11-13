"""
example48 - 字符串的操作

Author: larry
Date: 10/15/22

"""
email = "  l91liliang@gamil.com   "  # 多敲了空格
content = '  马化腾是个傻逼'
print(email.strip())  # 修剪空格，但是不会修剪中间的空格。
print(email.lstrip())  # 修剪左空格，但是不会修剪中间的空格。
print(email.rstrip())  # 修剪右空格，但是不会修剪中间的空格。

# 将指定的字符串替换为新的内容，并去掉空格。
print(content.replace('马化腾', '*').replace('傻逼', '*').strip())
