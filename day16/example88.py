'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 20:08:09
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 20:18:47
FilePath: /PythonWork/day16/example88.py
Description: example88 - 文件操作（读取二进制文件（字节文件））
'''
file = open(file='resources/DSC_0218-copy(5).JPG', mode='rb')

# # 以下方法可以获取文件的字节数。
# # 移动文件指针
# file.seek(0, 2)
# # 通过tell方法查看文件指针移动的字节数
# print(file.tell())

try:
    # 如果读不到数据，read方法会返回NONE。
    data = file.read(1024)
    while data:
        print(file.read(1024), end='')  # 一次性读12个字符。
        data = file.read(1024)
finally:
    file.close()
