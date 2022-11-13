'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-10 21:06:10
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-10 21:16:49
FilePath: /PythonWork/day14/example82.py
Description: example82 - 枚举类型
'''
from enum import Enum


class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = 0, 1, 2, 3


for suite in Suite:
    print(suite, suite.value)
