'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 21:40:24
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 21:50:17
FilePath: /PythonWork/day16/example90.py
Description: example90 - 文件操作（写文本文件）
'''
import sys
file = open('resources/苟.txt', mode='w', encoding=sys.getdefaultencoding())
try:
    file.write('苟利国家生死以\r\n')
    file.write('岂因祸福避趋之')

finally:
    file.close()
