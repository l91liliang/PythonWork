'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-12 22:31:05
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 23:34:01
FilePath: /PythonWork/day16/example94.py
Description: example94 - 从文件中读入体温测量数据，显示温度不正常的病人的信息。

~ 37.2以下 ---> 正常
~ 37.2-38.5 --->偏高
~ 38.5以上 ---> 发热


'''
# # 随机生成temperature.txt文件
# from random import uniform
# with open('resources/temperature.txt', 'w') as file:
#     for i in range(100):
#         file.write(f'病人{i+1:0>3d} {round(uniform(36.0,39.0),1)}\r\n')

# #复制文件
# def file_copy(source_file, target_file):
#     with open(file=source_file, mode='rb') as source:
#         with open(target_file, 'wb') as target:
#             data = source.read(1024)
#             while data:
#                 # 更新数据
#                 target.write(data)
#                 data = source.read(1024)

# if __name__=='__main__':
#     file_copy('resources/temperature.txt','resources/temperature1.txt')
high = []
too_high = []

with open('resources/temperature1.txt', mode='r') as file:
    data = file.readline()  # 读文件时，最好一次读一行
    while data:
        no, temp = data.split()
        if float(temp) <= 37.2:
            pass
        elif float(temp) <= 38.5:
            high.append(no)
        else:
            too_high.append(no)
        data = file.readline()

print("偏高的病人有：")
print(high)
print("发热的病人有：")
print(too_high)
