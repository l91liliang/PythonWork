'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 21:29:55
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 21:37:15
FilePath: /PythonWork/day16/example89.py
Description: example89 - 读取文件的MD5、SHA256哈希码（签名、指纹、摘要）
'''

import hashlib

hasher = hashlib.md5()
hasher2 = hashlib.sha256()
file = open(file='resources/DSC_0218-copy(5).JPG', mode='rb')
try:
    # 如果读不到数据，read方法会返回NONE。
    data = file.read(1024)
    while data:
        # 更新数据
        hasher.update(data)
        hasher2.update(data)
        data = file.read(1024)
finally:
    file.close()

# 获得十六进制形式的MD5哈希摘要
print(hasher.hexdigest())

# 获得十六进制形式的SHA256哈希摘要
print(hasher2.hexdigest())
