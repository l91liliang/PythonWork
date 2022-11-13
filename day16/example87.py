'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 19:08:27
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 19:50:38
FilePath: /PythonWork/day16/example87.py
Description: example87 - 文件操作
'''
import sys
print(sys.getdefaultencoding())
file = open(file='resources/第21课：文件读写和异常处理.md',
            mode='r', encoding=sys.getdefaultencoding())
try:
    #如果读不到数据，read方法会返回NONE。
    data=file.read(12)
    while data:
        print(file.read(12), end='')  # 一次性读12个字符。
        data=file.read(12) 
except:
    print('读文件时发生错误。')
finally:  # 总是执行代码
    file.close()
