"""
example50 - 字符串的操作

编码--->把一种字符集转换成另外一种字符集    str（字符串）--->encode（字符集）--->bytes（字节串）
解码--->bytes（字节串）--->decode()--->str（字符串）

要点：
1.选择字符集（编码）的时候，最佳的选择（也就是默认的）是UTF-8编码。
2.编码和解码的字符集要保持一致，否则就会出现乱码现象。
3.不能用ISO-8859-1编码保存中文，否则会出现编码黑洞，中文变成？。
4.UTF-8是Unicode的一种实现方案，也是一种变长的编码，
最少1个字节（英文和数字），最多4个字节（Emoji），表示中文用3个字节。

百分号编码--->
BASE64编码--->

Author: larry
Date: 10/17/22

"""
# a = '不做奴才做公民'
# # GBK<---GB2312<---ASCII，GBK编码中，1个中文字符等于2个字节。
# b = a.encode('gbk')
# print(type(b))
# print(b, len(b))
#
# c = b'\xb2\xbb\xd7\xf6\xc5\xab\xb2\xc5\xd7\xf6\xb9\xab\xc3\xf1'
# d = c.decode('gbk')
# print(d)

a = '不做奴才做公民😇😇😇🐻🐻🐻1a'
# GBK<---GB2312<---ASCII
# UTF-8编码是Unicode（万国码）的一种实现方案，此编码中，1个中文字符等于3个字节，1个Emoji字符等于4个字节，1个数字和英文字母的时候等于1个字节。。
b = a.encode('utf-8')
print(type(b))
print(b, len(b))

c = b'\xe4\xb8\x8d\xe5\x81\x9a\xe5\xa5\xb4\xe6\x89\x8d\xe5\x81\x9a\xe5\x85\xac\xe6\xb0\x91\xf0\x9f\x98\x87\xf0\x9f\x98\x87\xf0\x9f\x98\x87\xf0\x9f\x90\xbb\xf0\x9f\x90\xbb\xf0\x9f\x90\xbb'
# 如果编码和解码的方式不一致，Python中可能会产生UnicodeDecodeError错误

d = c.decode('utf-8')
print(d)

'''
编码黑洞，完全不能用某一种编码格式编码。UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-6: ordinal not in range(256)
'''
# a = '不做奴才做公民'
# b = a.encode('iso-8859-1')
# print(b, len(b))
