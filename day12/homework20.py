"""
homework20 - 写一个实现生成指定长度的随机验证码（由数字、标点和英文字母构成）的函数

Author: larry
Date: 10/25/22

"""
import random
import string

ALL_CHARS = string.digits + string.ascii_letters + string.punctuation


def generate_code(code_len: int = 6) -> str:  # 可以在定义函数时，加上类型标注，如int、str等
    """
    密码生成器

    :param code_len:生成密码的长度
    :return: 生成的密码
    """

    return ''.join(random.choices(ALL_CHARS, k=code_len))


M = int(input("请输入要生成的密码长度："))
print(f"密码为：{generate_code(M)}")
