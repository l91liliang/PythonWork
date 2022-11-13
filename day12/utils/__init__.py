"""
__init__.py - 包的初始化文件（导入包的时候会自动执行此文件）

任务：写一个函数，传入一个文件名（字符串），返回这个文件的后缀名
hello.py--->.py
hello.py.txt--->.txt
.abc--->没有后缀名（返回空字符串）
abc.--->没有后缀名（返回空字符串）

Author: larry
Date: 10/29/22

"""


def get_suffix(filename: str, *, has_dot: bool = False) -> str:
    """
    获取文件的后缀名

    :param filename:文件名字符串
    :param has_dot: 是否显示.，默认不显示
    :return: 返回文件后缀名
    """
    # 从字符串中逆向查找.出现的位置
    pos = filename.rfind('.')
    # 通过切片操作从文件名中取出后缀名
    if pos <= 0:
        return ''
    if not has_dot:
        pos = pos + 1
    return filename[pos:]
