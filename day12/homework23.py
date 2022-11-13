"""
homework23 - 设计获得样本数据描述性统计信息的函数

集中趋势：均值、中位数、众数
离散趋势：极差、方差、标准差

Author: larry
Date: 10/29/22

"""
import random

import math


def ptp(data):
    """求极差"""
    return max(data) - min(data)


def average(data):
    """求平均数"""
    return sum(data) / len(data)


def var(data):
    """求方差"""
    x_bar = average(data)
    temp = [(x - x_bar) ** 2 for x in data]
    return sum(temp) / (len(temp) - 1)


def std(data):
    """求标准差"""
    return math.sqrt(var(data))


def med(data):
    """求中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return average(temp[size // 2 - 1:size // 2 + 1])


# __name__是一个隐藏变量，它代表了当前模块（文件）的名字。
# 如果直接通过Python解释器运行homework23.py文件，__name__的值是__main
# 如果是在其他模块（文件）中导入homework23文件，那么__name__的值是homework23
if __name__ == '__main__':
    data = [random.randint(1, 101) for _ in range(10)]
    print(
        f"数列{data}的极差：{ptp(data)}、平均数：{average(data)}、方差：{var(data)}、标准差：{std(data)}、中位数：{med(data)}。")
