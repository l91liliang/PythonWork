"""
example33 - 显示所有的汉字

汉字的编码范围0x4e00~0x9fa5
ord()--->函数查看字符对应的编码
chr()--->将编码处理成对应的字符

Author: larry
Date: 10/7/22

"""
for x in range(0x4e00, 0x9fa5):
    print(chr(x), end='')
