"""
example42 - 字符串

Author: larry
Date: 10/13/22

"""
a = 'hello world'
b = "hello world"
c = '''
\"hello\tabc
world\"
'''  # 转义字符
print(c)
d = r'''
\"hello\tabc
world\"
'''  # 在字符串前加r表示原始字符串，不转义。
print(d)

s1 = '\141\142\143\x61\x62\x63'
print(s1)

# ASCII--->GB2312--->GBK--->Unicode(UTF-8)，Unicode较为国际化。
s2 = '\u674e\u4eae'  # 转义Unicode编码
print(s2)
