"""
example51 - 字符串的操作
凯撒密码 - 通过对应字符的替换，实现对明文进行加密的一种方式。

abcdefghijklmnopqrstuvwxyz
defghijklmnopqrstuvwxyzabc

明文：attack at dawn
密文：dwwdfn dw gdzq

对称加密：加密和解密使用了相同的密钥--->AES
非对称加密：加密和解密使用不同的密钥（公钥、私钥）--->RSA--->适合互联网应用。

Author: larry
Date: 10/17/22

"""
message = 'attack at dawn'
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyzabc")  # 生成字符转换的对照表。

print(message.translate(table))  # 通过字符串的translate方法实现字符串转译。
