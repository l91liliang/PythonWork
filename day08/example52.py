"""
example52 - 字符串：生成随机验证码

Author: larry
Date: 10/17/22

"""
import random
import string

# nums = [i for i in '0123456789']
# big_letters = [chr(i) for i in range(65, 91)]
# small_letters = [chr(i) for i in range(97, 123)]
# all_chars = nums + big_letters + small_letters
# all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_chars = string.digits + string.ascii_letters

for _ in range(10):
    # 可迭代对象
    selected_chars = random.choices(all_chars, k=4)  # choice中k的默认值为1。
    print(''.join(selected_chars))
