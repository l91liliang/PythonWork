'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 22:20:35
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 22:30:18
FilePath: /PythonWork/day16/example93.py
Description: 将100以内的质数输出到文件中每行一个数
'''
import sys
with open(file='resources/质数.txt', mode='w', encoding=sys.getdefaultencoding()) as file:
    file.write('以下为100以内的所有质数：\r\n')
    for a in range(2, 101):
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
        if is_prime:
            file.write(str(a)+'\r\n')
