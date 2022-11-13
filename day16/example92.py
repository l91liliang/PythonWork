'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 22:01:45
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 22:07:43
FilePath: /PythonWork/day16/example92.py
Description: 文件复制
'''


def file_copy(source_file, target_file):
    with open(file=source_file, mode='rb') as source:
        with open(target_file, 'wb') as target:
            data = source.read(1024)
            while data:
                # 更新数据
                target.write(data)
                data = source.read(1024)

if __name__=='__main__':
    file_copy('resources/苟.txt','poem.txt')