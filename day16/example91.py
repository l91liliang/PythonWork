'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 21:40:24
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 22:00:31
FilePath: /PythonWork/day16/example90.py
Description: example91 - 文件操作（写文本文件），添加文本
'''
import sys
# with - 上下文语法 - 进入和离开with的时候会自动执行某些操作
# 下面的写法在离开with上下文的时候，会自动执行file对象的close()方法。建议用以下方法
with open('resources/苟.txt', mode='a', encoding=sys.getdefaultencoding()) as file:
    file.write('————江泽民')
