#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example71.py - 编写实现对列表元素进行冒泡排序的函数
@Time    :   2022/10/31 21:35:53
@Author  :   Larry 
@Version :   1.0
@Contact :   l91liliang@hotmail.com
@License :   
@Desc    :   None
设计函数的时候，一定要注意函数的无副作用性（调用函数不影响传入的参数）
'''

# here put the import lib


def bubble_soft(items: list, ascending=True, gt=lambda x, y: x > y) -> list:
    """
    冒泡排序

    :param items: 待排序的列表
    :param ascending: 是否使用升序
    :param gt: 比较两个元素大小的函数
    :return: 排序后的列表
    """
    for i in range(1, len(items)):
        items = items[:]
        for j in range(0, len(items)-i):
            if gt(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    if not ascending:
        items = items[::-1]
    return items


if __name__ == '__main__':
    nums = [1, 9, 8, 4, 5, 7, 6, 2, 3]
    print(bubble_soft(nums))
    print(bubble_soft(nums, ascending=False))
    print(nums)
    words = ['banana', 'apple', 'orange', 'watermelon', 'hello']
    print(bubble_soft(words, gt=lambda x, y: len(x) > len(y), ascending=False))
