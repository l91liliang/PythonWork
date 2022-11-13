"""
example44 - 字符串的索引和切片

跑马灯文字效果
清除屏幕输出：Windows--->cls//macOS--->clear

Author: larry
Date: 10/15/22

"""
import time
import os

content = "不要核酸要吃饭，不要封控要自由                       "
'''
content = "不要核酸要吃饭，不要封控要自由                       "
content = "要核酸要吃饭，不要封控要自由                       不"
content = "核酸要吃饭，不要封控要自由                       不要"
content = "酸要吃饭，不要封控要自由                       不要核"
content = "要吃饭，不要封控要自由                       不要核酸"
......
'''
while True:
    os.system('clear')
    print(content)
    time.sleep(0.3)  # 休眠操作-让程序暂停0.5s
    content = content[1:] + content[0]

# a = 'hello,world'
# # 索引
# print(a[0], a[-len(a)])
# print(a[len(a) - 1], a[-1])
# print(a[5], a[-6])
#
# # 切片
# print(a[2:5])
# print(a[1:10:2])
# print(a[::-1])
